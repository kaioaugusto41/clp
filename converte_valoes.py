
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

def converte_valores(valor):
    valor = BinaryPayloadDecoder.fromRegisters(valor.registers, Endian.Big, wordorder=Endian.Little)      # O valor retornado será convertido        
    valor_convertido = "%.2f" % valor.decode_32bit_float()
    return valor_convertido   