A+[A-Z]+K[0-9] 

{"StartingState": "S2", "S0": {"isTerminatingState": false, "A": "S1"}, "S1": {"isTerminatingState": false, "epsilon": ["S3", "S2"]}, "S2": {"isTerminatingState": false, "epsilon": "S0"}, "S3": {"isTerminatingState": false, "epsilon": "S6"}, "S4": {"isTerminatingState": false, "[A-Z]": "S5"}, "S5": {"isTerminatingState": false, "epsilon": ["S7", "S6"]}, "S6": {"isTerminatingState": false, "epsilon": "S4"}, "S7": {"isTerminatingState": false, "epsilon": "S8"}, "S8": {"isTerminatingState": false, "K": "S9"}, "S9": {"isTerminatingState": false, "epsilon": "S10"}, "S10": {"isTerminatingState": false, "[0-9]": "S11"}, "S11": {"isTerminatingState": true}}



A+[A-Z]+K

{"StartingState": "S2", "S0": {"isTerminatingState": false, "A": "S1"}, "S1": {"isTerminatingState": false, "epsilon": ["S3", "S2"]}, "S2": {"isTerminatingState": false, "epsilon": "S0"}, "S3": {"isTerminatingState": false, "epsilon": "S6"}, "S4": {"isTerminatingState": false, "[A-Z]": "S5"}, "S5": {"isTerminatingState": false, "epsilon": ["S7", "S6"]}, "S6": {"isTerminatingState": false, "epsilon": "S4"}, "S7": {"isTerminatingState": false, "epsilon": "S8"}, "S8": {"isTerminatingState": false, "K": "S9"}, "S9": {"isTerminatingState": true}}

A+[A-Z]A 

{"StartingState": "S2", "S0": {"isTerminatingState": false, "A": "S1"}, "S1": {"isTerminatingState": false, "epsilon": ["S3", "S2"]}, "S2": {"isTerminatingState": false, "epsilon": "S0"}, "S3": {"isTerminatingState": false, "epsilon": "S4"}, "S4": {"isTerminatingState": false, "[A-Z]": "S5"}, "S5": {"isTerminatingState": false, "epsilon": "S6"}, "S6": {"isTerminatingState": false, "A": "S7"}, "S7": {"isTerminatingState": true}}


a*(a|b)aa

{"StartingState": "S2", "S0": {"isTerminatingState": false, "a": "S1"}, "S1": {"isTerminatingState": false, "epsilon": ["S3", "S2"]}, "S2": {"isTerminatingState": false, "epsilon": ["S0", "S3"]}, "S3": {"isTerminatingState": false, "epsilon": "S8"}, "S4": {"isTerminatingState": false, "a": "S5"}, "S5": {"isTerminatingState": false, "epsilon": "S9"}, "S6": {"isTerminatingState": false, "b": "S7"}, "S7": {"isTerminatingState": false, "epsilon": "S9"}, "S8": {"isTerminatingState": false, "epsilon": ["S6", "S4"]}, "S9": {"isTerminatingState": false, "epsilon": "S10"}, "S10": {"isTerminatingState": false, "a": "S11"}, "S11": {"isTerminatingState": false, "epsilon": "S12"}, "S12": {"isTerminatingState": false, "a": "S13"}, "S13": {"isTerminatingState": true}}


(a|b)*a(a|b)(a|b)

{"StartingState": "S6", "S0": {"isTerminatingState": false, "a": "S1"}, "S1": {"isTerminatingState": false, "epsilon": "S5"}, "S2": {"isTerminatingState": false, "b": "S3"}, "S3": {"isTerminatingState": false, "epsilon": "S5"}, "S4": {"isTerminatingState": false, "epsilon": ["S2", "S0"]}, "S5": {"isTerminatingState": false, "epsilon": ["S7", "S6"]}, "S6": {"isTerminatingState": false, "epsilon": ["S4", "S7"]}, "S7": {"isTerminatingState": false, "epsilon": "S8"}, "S8": {"isTerminatingState": false, "a": "S9"}, "S9": {"isTerminatingState": false, "epsilon": "S14"}, "S10": {"isTerminatingState": false, "a": "S11"}, "S11": {"isTerminatingState": false, "epsilon": "S15"}, "S12": {"isTerminatingState": false, "b": "S13"}, "S13": {"isTerminatingState": false, "epsilon": "S15"}, "S14": {"isTerminatingState": false, "epsilon": ["S12", "S10"]}, "S15": {"isTerminatingState": false, "epsilon": "S20"}, "S16": {"isTerminatingState": false, "a": "S17"}, "S17": {"isTerminatingState": false, "epsilon": "S21"}, "S18": {"isTerminatingState": false, "b": "S19"}, "S19": {"isTerminatingState": false, "epsilon": "S21"}, "S20": {"isTerminatingState": false, "epsilon": ["S18", "S16"]}, "S21": {"isTerminatingState": true}}


