"""Small UI state helper: manage simple UI states and transitions."""

class UIStateHelper:
    def __init__(self):
        self._states = set()
        self._transitions = {}
        self.current = None

    def add_state(self, name):
        self._states.add(name)

    def add_transition(self, from_state, to_state):
        if from_state not in self._states or to_state not in self._states:
            raise ValueError("Both states must be added first")
        self._transitions.setdefault(from_state, set()).add(to_state)

    def set_start(self, name):
        if name not in self._states:
            raise ValueError("State not known")
        self.current = name

    def can_transition(self, to_state):
        return to_state in self._transitions.get(self.current, set())

    def transition(self, to_state):
        if not self.can_transition(to_state):
            raise ValueError(f"Cannot transition from {self.current} to {to_state}")
        self.current = to_state

    def __repr__(self):
        return f"<UIStateHelper current={self.current}>"

if __name__ == "__main__":
    ui = UIStateHelper()
    for s in ("home", "settings", "about"):
        ui.add_state(s)
    ui.set_start("home")
    ui.add_transition("home", "settings")
    ui.add_transition("settings", "about")
    ui.add_transition("about", "home")
    print(ui)
    for next_state in ("settings", "about", "home"):
        ui.transition(next_state)
        print(ui)