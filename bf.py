class BFRunner():
    def __init__(self, instr, mem = 4096):
        self.ptr = 0
        self.memory = [0] * mem
        self.instr = 0
        self.program = self.parse(instr)

    def exec(self):
        while self.instr < len(self.program):
            self.program[self.instr].execute(self)
            self.instr += 1

        return self.memory[self.ptr]

    def parse(self, instr):
        asm = []
        loopstack = []

        carryInstr = None
        for cod in instr:
            if   cod == '>':
                if isinstance(carryInstr, BFPtrMov):
                    carryInstr.val += 1
                else:
                    if carryInstr != None: asm.append(carryInstr)
                    carryInstr = BFPtrMov(+1)
            elif cod == '<':
                if isinstance(carryInstr, BFPtrMov):
                    carryInstr.val -= 1
                else:
                    if carryInstr != None: asm.append(carryInstr)
                    carryInstr = BFPtrMov(-1)

            elif cod == '+':
                if isinstance(carryInstr, BFIncDec):
                    carryInstr.val += 1
                else:
                    if carryInstr != None: asm.append(carryInstr)
                    carryInstr = BFIncDec(+1)
            elif cod == '-':
                if isinstance(carryInstr, BFIncDec):
                    carryInstr.val -= 1
                else:
                    if carryInstr != None: asm.append(carryInstr)
                    carryInstr = BFIncDec(-1)

            elif cod == '[':
                if carryInstr != None:
                    asm.append(carryInstr)
                    carryInstr = None

                loopstack.append(len(asm) - 1)
            elif cod == ']':
                if carryInstr != None:
                    asm.append(carryInstr)
                    carryInstr = None

                asm.append(BFJmpIf(loopstack.pop()))

            elif cod == '.':
                if carryInstr != None:
                    asm.append(carryInstr)
                    carryInstr = None

                asm.append(BFPut())

            elif cod == ',':
                raise "Unimplemented"

            else: pass # comments

        if carryInstr != None:
            asm.append(carryInstr)
            carryInstr = None # eh

        return asm


# > 	ptr++;
# < 	ptr--;
# + 	++(*ptr);
# - 	--(*ptr);
# . 	putchar(*ptr);
# , 	(*ptr) = getchar();
# [ 	while(*ptr) {
# ] 	}

class BFIncDec():
    def __init__(self, amount):
        self.val = amount

    def execute(self, state: BFRunner):
        state.memory[state.ptr] += self.val
        state.memory[state.ptr] %= 256

class BFPtrMov():
    def __init__(self, amount):
        self.val = amount

    def execute(self, state: BFRunner):
        state.ptr += self.val


class BFPut():
    def execute(self, state: BFRunner):
        print(chr(state.memory[state.ptr]), end = '')

class BFJmpIf():
    def __init__(self, ptr):
        self.jmp = ptr

    def execute(self, state: BFRunner):
        if state.memory[state.ptr] != 0:
            state.instr = self.jmp

BFRunner(
    """++++[++++>---<]>-.-[--->+<]>++++.-.+++++.----.------.+++++++++.[-->+++++<]>+++.>-[--->+<]>.--[--->+<]>-.+++++++++.[--->++++<]>.[------>+<]>-.++[--->++<]>.[-->+<]>-.+."""
).exec()