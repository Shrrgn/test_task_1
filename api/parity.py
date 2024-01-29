from api.enums import ColorTypes


class ParityChecker:
    def check_parity(self, value: int) -> ColorTypes:
        return ColorTypes.GREEN if value % 2 == 0 else ColorTypes.RED
