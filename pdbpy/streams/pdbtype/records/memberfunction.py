from ctypes import sizeof as c_sizeof

from dtypes.structify import structify
from dtypes.typedefs import uint8_t, uint16_t, uint32_t

from .base import record, PackedStructy, buffy, FunctionAttributes
from ..leaf_enum import LeafID
from ...typing import type_index

@record(LeafID.MFUNCTION)
@structify
class MemberFunction(PackedStructy):
    record_type     : uint16_t
    return_type     : type_index
    class_type      : type_index
    this_ptr_type   : type_index
    call_convention : uint8_t
    attributes      : FunctionAttributes
    parameter_count : uint16_t
    arg_list        : type_index
    this_adjustment : uint32_t


    @classmethod
    def from_memory(cls, mem, offset, record_size : 'Optional[int]', debug : bool):
        my_size = c_sizeof(cls)
        self = cls.from_buffer_copy(buffy(mem, offset, offset + my_size))
        self.addr = offset

        post_read_offset = offset + my_size

        return post_read_offset, self