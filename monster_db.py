# Qua e dove terro tutti i dati per la creazione dei mostri, i dati vengono
# dal manuale dei mostri
# "might":8,"dexterity":8,"insight":8,"will":8
import random

affinities_list = [
    "physical", "air", "bolt", "dark", "earth", "fire", "ice", "light", "poison" 
]
affinities_list_ita = [
    "fisico", "aria", "fulmine", "ombra", "terra", "fuoco", "ghiaccio", "luce", "veleno" 
]
species_list = [
    "Beast", "Construct", "Demon", "Elemental", "Humanoid", "Monster", "Plant", "Undead"
]
statuses_list = [
    "slow", "dazed", "weak", "shaken", "enraged", "poisoned"
]

#incantesimi
def soffio(monster):
    print("soffio")

    monster["spells"].append({
      "target": "Una creatura",
      "duration": "Istantanea",
      "attr1": "insight",
      "attr2": "will",
      "name": "Soffio",
      "itemType": "spell",
      "damagetype": "physical",
      "mp": "5",
      "maxTargets": 1,
      "type": "offensive",
      "effect": "Il bersaglio subisce **【 TM + 10】** danni da **" + 
      affinities_list_ita[random.randint(0, (len(affinities_list_ita)- 1))] + "**."
      ,
    },)

def collera(monster):
    print("Collera")

    monster["spells"].append({
      "target": "Una creatura",
      "duration": "Istantanea",
      "attr1": "insight",
      "attr2": "will",
      "name": "Collera",
      "itemType": "spell",
      "damagetype": "physical",
      "mp": "10",
      "maxTargets": 1,
      "type": "offensive",
      "effect": "Spingi una creatura a perdere qualsiasi contegno e agire in maniera vventata. "
      "Il bersaglio subisce lo status **furente** e non può eseguire azioni di **Guardia** "
      "e **Incantesimo** nel suo prossimo turno."
      ,
    },)

def divoracorpo(monster):
    print("Divoracorpo")

    monster["spells"].append({
      "target": "Una creatura",
      "duration": "Istantanea",
      "attr1": "insight",
      "attr2": "will",
      "name": "Divoracorpo",
      "itemType": "spell",
      "damagetype": "physical",
      "mp": "10",
      "maxTargets": 1,
      "type": "offensive",
      "effect": "Il bersaglio subisce [**TM + 15**] danni da **" +
      affinities_list_ita[random.randint(0, (len(affinities_list_ita)- 1))] +
      "** e il PNG recupera un ammontare di Punti Vita pari a metà dei Punti Vita persi dal bersaglio."
      ,
    },)

def divoramente(monster):
    print("Divoramente")

    monster["spells"].append({
      "target": "Una creatura",
      "duration": "Istantanea",
      "attr1": "insight",
      "attr2": "will",
      "name": "Divoramente",
      "itemType": "spell",
      "damagetype": "physical",
      "mp": "10",
      "maxTargets": 1,
      "type": "offensive",
      "effect": "Il bersaglio subisce [**TM + 15**] danni da **" +
      affinities_list_ita[random.randint(0, (len(affinities_list_ita)- 1))] +
      "** e il PNG recupera un ammontare di Punti Mente pari a metà dei Punti Vita persi dal bersaglio."
      ,
    },)

#funzioni delle skills
def armatura_speciale(monster):
    print("Armatura Speciale")
    tipi = ["attacchi", "incantesimi", "abilità"]
    tipo = tipi[random.randint(0, (len(tipi)- 1))]

    monster["special"].append({
        "effect": "Finché questo PNG non è in Crisi, riduce tutti i danni che subisce da "
        +  tipo + " di 5 (prima delle Affinità).",
        "name": "Armatura Speciale"
    })

def attacco_vendicativo(monster):
    print("Attacco Vendicativo")

    monster["special"].append({
        "effect": "Quando un nemico riduce questo PNG a 0 PV, questo PNG esegue un **attacco potente** contro quel nemico. " +
        "Considera il **Tiro Maggiore** del Test di Precisione pari a 0 quando determini il danno inflitto da questo attacco.",
        "name": "Attacco Vendicativo"
    })
    
def caratteraccio(monster):
    print("Caratteraccio")
    casistiche = [
        "**è immune a tutti gli status eccetto furente.**",
        "**infligge 5 danni extra con l'attacco normale.**"
    ]

    monster["special"].append({
        "effect": "Finchè questo PNG è in **Crisi**, " + casistiche[random.randint(0, (len(casistiche)- 1))],
        "name": "Caratteraccio"
    })

def danni_collaterali(monster):
    print("Danni Collaterali")

    monster["special"].append({
        "effect": "Quando questo PNG ha succeso in un'azione di **intralcio**, può infliggere anche 10 " +
        "danni da " + affinities_list[random.randint(0, (len(affinities_list) - 1))] +
        " al bersaglio. Infligge 10 danni extra se questo PNG è di **livello 30 o superiore**.",
        "name": "Danni Collaterali"
    })

def duro_a_morire(monster):
    print("Duro a Morire")

    monster["special"].append({
        "effect": "Quando questo PNG vienne ridotto a 0 Punti VIta per la prima volta durante una scena, "+
        "è invece ridotto esattamente a 1 Punto Vita.",
        "name": "Duro a Morire"
    })

def aggiungi_immunita(monster):
    print("Aggiungi Immunità")
    valid_list = []

    for chiave, valore in monster["immunities"].items():
        if valore == "":
            valid_list.append(chiave)

    # scelgo X chiavi a caso (senza ripetizioni)
    scelte = random.sample(valid_list, min(2, len(valid_list)))

    # aggiorno il dizionario
    for chiave in scelte:
        monster["immunities"][chiave] = "true"
    
def attacco_normale_magico(monster):
    print("Attacco Normale Magico")

    monster["attacks"][0]["special"].append("Questo attacco bersaglia la **Difesa Magica** del bersaglio. ")

def attacco_potente_distante(monster):
    print("Attacco Distante Potente")
    status = ["**confuso**", "**debole**", "**lento**", "**scosso**"]

    monster["attacks"][1]["range"] = "distance"
    monster["attacks"][1]["attr1"] = "dexterity"
    monster["attacks"][1]["special"].append("Poi i nemici colpiti subiscono lo status " + status[random.randint(0, (len(status) - 1))])

def crollo(monster):
    print("crollo")

    monster["special"].append({
        "effect": "Quando l’attacco potente manca tutti i bersagli, riempi 1 sezione di un Orologio da 6 chiamato "
        "“Crollo”. Poi, se l’Orologio “Crollo” è pieno, questo PNG perde quest’Abilità e ogni creatura "
        "in scena subisce un ammontare minore di danni da "
        + affinities_list_ita[random.randint(0, (len(affinities_list_ita) - 1))] + ".",
        "name": "Crollo"
    })

def impara_due_incantesimi(monster):
    print("impara due incantesimi")

bruto = {
    "stats": {   
        "dexterity": 8,
        "insight": 6,
        "might": 10,
        "will": 8
    },
    "vul_quantity": 2,
    "res_quantity": 0,
    "imm_quantity": 0,
    "customization": [],
    "skills": [
        {
            "name": "Armatura Speciale",
            "fun": armatura_speciale
        }
    ]
}


mago = {
    "stats": {   
        "dexterity": 8,
        "insight": 8,
        "might": 6,
        "will": 10
    },
    "vul_quantity": 1,
    "res_quantity": 0,
    "imm_quantity": 0
}  

mago_skills = {
    0: {
        "skill_name": "Danni Collaterali",
        "skill_text": "Quando fa intralcio infligge 10 danni di un tipo."
    },
    1: {
        "skill_name": "Esplosione Spirituale",
        "skill_text": "Quando si arrende da 10 punti menti a tutti i suoi alleati."
    }
}