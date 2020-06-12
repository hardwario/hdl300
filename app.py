import click
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

with open('version.txt') as f:
    version = f.read().strip()

def read_hr(client, address):
    result = client.read_holding_registers(address=address, count=1, unit=0x01)
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    return decoder

@click.command()
@click.option('-d', '--device', required=True, type=click.Path(exists=True), help='Specify device path.')
@click.version_option(version=version)
def main(device):

    mb = ModbusSerialClient(method='rtu', port=device, baudrate=9600, bytesize=8, parity='N', stopbits=1)
    connection = mb.connect()

    unit = read_hr(mb, 2).decode_16bit_uint()
    unit = ['', ' cm', ' mm', ' MPa', ' Pa', ' kPa', ' MA'][unit]

    divisor = read_hr(mb, 3).decode_16bit_uint()
    divisor = [1.0, 10.0, 100.0, 1000.0][divisor]

    value = read_hr(mb, 4).decode_16bit_int()

    click.echo('Pressure: {}{}'.format(value / divisor, unit))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
