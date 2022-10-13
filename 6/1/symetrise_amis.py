def symetrise_amis(direct, mode):
    for ami in direct:
        amis = direct[ami]
        for autre in amis.copy():
            if mode: direct[autre] |= {ami}
            elif ami not in direct[autre]: amis -= {autre}

    # return direct