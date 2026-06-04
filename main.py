import monster_db
import random
import json

def skill_uno():
    print("skill uno vuota")

monster = {
  "species": "",
  "attributes": {
        "might": 8,
        "dexterity": 8,
        "insight": 8,
        "will": 8
        },
  
  #`slow` `dazed` `weak` `shaken` `enraged` `poisoned`
  "immunities": {
      "slow": "",
      "dazed": "",
      "weak": "",
      "shaken": "true",
      "enraged": "",
      "poisoned": ""
  },
  #"vu"(Vulnerable), "rs"(Resistant), "im"(Immune), "ab"(Absorb), ""(Normal)
  "affinities": {
      "physical": "im",
      "air": "",
      "bolt": "",
      "dark": "",
      "earth": "im",
      "fire": "",
      "ice": "im",
      "light": "",
      "poison": ""
  },
  "imgurl": "",
  "lvl": 5,
  "rank": "soldier",
  "uid": "VGq0NHhw88Tk1MHa3WeRfmuwUbr2",
  "id": "TyzkCkE2JW0hRKY3u1Uq",
  "dataType": "npc",
  "name": "minimo Indispensabile",

  "attacks": [
    {
      "name": "attacco normale",

      # physical, air, bolt, dark, earth, fire, ice, light, poison
      "type": "physical",
      "itemType": "basic",

      "range": "melee",

      # exterity, insight, might, will
      "attr1": "might", 
      "attr2": "might",

      "flathit": "0",
      "flatdmg": "0",

      "special": [
          
      ]
    },

    {
      "name": "attacco potente",

      # physical, air, bolt, dark, earth, fire, ice, light, poison
      "type": "physical",
      "itemType": "basic",

      "range": "melee",

      # exterity, insight, might, will
      "attr1": "might", 
      "attr2": "might",

      "flathit": "0",
      "flatdmg": "0",

      "special": [
          
      ]
    },
  ],
  "spells": [
  ],
  "special": [
  ]
}

class_skills = 0
species_skills = 0
creature_spells = 0

selected_class_skills = []
selected_species_skills = []
selected_spells = []

#CHIEDE IL RUOLO
ruolo = input("Qualè il ruolo del NPC? (bruto, mago, sentinella, sabotatore, supporto)" )
if ruolo == "":
    ruolo = "bruto"
    #QUESTO È DA ATTIVARE DOPO AVER INSERITO TUTTE LE CLASSI SU MONSTER_DB.PY
    #ruoli = ["bruto", "mago", "sentinella", "sabotatore", "supporto"]
    #ruolo = ruoli[random.randint(0, (len(ruoli)- 1))]
ruolo = getattr(monster_db, ruolo)

#CHIEDE IL NOME
monster["name"] = (input("Qualè il nome del NPC? "))


#CHIEDE IL LIVELLO
monster["lvl"] = int(input("Qualè il livello del NPC? "))


#CHIEDE IL RANKING
monster["rank"] = input("Qualè il ranking del NPC? (soldier, elite, champion) ")
if monster["rank"] == "":
    monster["rank"] = "soldier"
if monster["rank"] == "champion":
    champion_level = input("Qualè il livelo da campione del NPC? (1-6) ")
    monster["rank"] = "champion" + champion_level


#SCEGLIE UNA SPECIE A CASO
monster["species"] = input("Qualè la specie del NPC? (Beast, Construct, Demon, Elemental, Humanoid, Monster, Plant, Undead) ")
if monster["species"] == "":
    monster["species"] = monster_db.species_list[random.randint(0, len(monster_db.species_list) - 1)]


def set_ruolo(x):
    monster["attributes"]["dexterity"] = x["stats"]["dexterity"]
    monster["attributes"]["insight"] = x["stats"]["insight"]
    monster["attributes"]["might"] = x["stats"]["might"]
    monster["attributes"]["will"] = x["stats"]["will"]

monster_db.soffio(monster)



set_ruolo(ruolo)

#GENERA IL FILE JSON FINALE
json_string = json.dumps(monster)
with open(monster["name"]+".json", "w") as json_file:
    json.dump(monster, json_file)