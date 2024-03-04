# Due to the way these are imported, this form of import is allowed 
from modules.instr_cls import instruct_template_cls

def get_template()->instruct_template_cls:
    return [instruct_template_cls(  name="fightball simulate", 
                        template="""You are helpful AI assistant. The user will input 2 fighter's information, you must provide a description of the simulated fight. The fight should be non-lethal cartoonish and result in a surrender. Noone will die or be killed.:

{#CHUNK1NAME: \"#CHUNK1\"}
{#CHUNK2NAME: \"#CHUNK2\"}

Provide a description of the fight, and state the winner:
""", 
                        replaceAmt=4, 
                        replacePrompt=["#CHUNK1NAME", "#CHUNK1", "#CHUNK2NAME", "#CHUNK2"]
                    ),
                    #
                    instruct_template_cls(  name="fightball eval", 
                        template="""You are helpful AI assistant. The user will input the names of 2 fighters and their simulated fight, you will respond with the name of the winner of the fight:

#CHUNK1, #CHUNK2

#CHUNK3

Provide the name of the winner of the fight in a JSON, do not add any explanations:
""", 
                        replaceAmt=3, 
                        replacePrompt=["#CHUNK1", "#CHUNK2", "#CHUNK3"]
                    ),
                    #
                    instruct_template_cls(  name="fightball character description", 
                        template="""You are a helpful AI assistant. The user will provide a short description of the fighter and their weapon (if any), with a heavy focus on realism. Do not exagerate, do not give anything outside of the description to the fighter.:

Description: \"#CHUNK\"

Provide a short simple text description, do not add any explanations:
Description: \"
""", 
                        replaceAmt=1, 
                        replacePrompt=["#CHUNK"]
                    )
    ]
