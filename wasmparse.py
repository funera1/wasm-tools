from wasm_tob import (
    decode_module,
    decode_bytecode,
    format_instruction,
    format_lang_type,
    format_mutability,
    SEC_DATA,
    SEC_ELEMENT,
    SEC_GLOBAL,
    SEC_CODE,
)

with open('./binary-trees.wasm', 'rb') as raw:
    raw = raw.read()

mod_iter = iter(decode_module(raw))
header, header_data = next(mod_iter)

for cur_sec, cur_sec_data in mod_iter:
    if cur_sec_data.id == SEC_CODE:

        for i, entry in enumerate(cur_sec_data.payload.bodies):
            print(f"cur_func_idx: {i}")
            code_iter = iter(decode_bytecode(entry.code))

            wasm_pos = 0
            for op, imm, ofs in code_iter:
                print(f"(opcode, wasm_pos): {hex(op.id), wasm_pos}")
                wasm_pos += ofs
                # print(op.mnemonic, wasm_pos)
            print("")

