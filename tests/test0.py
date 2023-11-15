
# json_obj = aleo2json("./hello/build/main.aleo")
import json 

json_obj = {"type":"ProgramCore","id":{"type":"ProgramID","name":"hello","network":"aleo"},"identifiers":{"hello":{"type":"ProgramDefinition","definition":"Function"}},"imports":{},"mappings":{},"structs":{},"records":{},"closures":{},"functions":{"hello":{"type":"FunctionCore","name":"hello","inputs":[{"type":"Input","register":{"type":"Register","vtype":"Locator","value":0},"value_type":{"type":"ValueType","vtype":"Public","value":{"type":"PlaintextType","vtype":"Literal","value":{"type":"LiteralType","name":"u32"}}},"str":"input r0 as u32.public;"},{"type":"Input","register":{"type":"Register","vtype":"Locator","value":1},"value_type":{"type":"ValueType","vtype":"Private","value":{"type":"PlaintextType","vtype":"Literal","value":{"type":"LiteralType","name":"u32"}}},"str":"input r1 as u32.private;"}],"instructions":[{"type":"Instruction","vtype":"Add","value":{"type":"Literals","operands":[{"type":"Operand","vtype":"Register","value":{"type":"Register","vtype":"Locator","value":0}},{"type":"Operand","vtype":"Register","value":{"type":"Register","vtype":"Locator","value":1}}],"destination":{"type":"Register","vtype":"Locator","value":2}},"str":"add r0 r1 into r2;"}],"outputs":[{"type":"Output","operand":{"type":"Operand","vtype":"Register","value":{"type":"Register","vtype":"Locator","value":2}},"value_type":{"type":"ValueType","vtype":"Private","value":{"type":"PlaintextType","vtype":"Literal","value":{"type":"LiteralType","name":"u32"}}},"str":"output r2 as u32.private;"}],"finalize_logic":"null"}}}

# with open("./main.json", "r") as f:
#     json_obj = json.load(f)


print(f"json_obj: {json_obj}")
insts = json_obj["functions"]["hello"]["instructions"]
print(insts)
result  =False 
for inst in insts:
    tokens  = inst["str"].strip(";").split()
    print(tokens)
    # match tokens:
    #     case ["div", r0, r1, "into", r3]:
    #         result = True
    #     case _:
    #         pass

    if tokens[0] =="div":
        result = True

print("Result: ",result)