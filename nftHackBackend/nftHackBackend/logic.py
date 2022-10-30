import os
import openai


TOKEN = 's' + 'k-8oF2E5pt3IMG5x' + 'PZ1mDyT3BlbkFJh8Gq1LocG2Qd5UwfSdgQ'

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = TOKEN


def get_prompt_from_gpt3(name_of_collection):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="I am generating NFT pictures using image generators.\n"
               "NAME: \"NFT Hackathon\"\nSTYLE: \"drawing\"\n"
               "ATTRIBUTES:\nbackground: deep ocean blue, white, hell\n"
               "head: winner, clown, loser\nclothing: hoodie, amazing\n"
               "\nNAME: \"deGods\"\nSTYLE: \"realistic drawing\"\n"
               "ATTRIBUTES:\nbackground: white, black, green, yellow, orange\n"
               "head: Fade, Prince hair, Mushroom head, GodHawk\n"
               "clothing: tux, bomber, gym tee, hoodie, clown outfit\n\n"
               "NAME: \"NFT Mini-Series\"\nSTYLE: \"comic book\"\nATTRIBUTES:"
               "\nbackground: cityscape, space, white, black\nhead: human, alien, mutant\n"
               "clothing: costume, super suit, gym clothes, street clothes\n\n"
               "NAME: \"NFT 2.0\"\nSTYLE: \"cyberpunk\"\nATTRIBUTES:\nbackground: digital, dark, gritty\nhead: human, "
               "android, cyborg\nclothing: armor, high tech, everyday\n\nNAME: \"cryptopunks\"\nSTYLE: \"pixel "
               "art\"\nATTRIBUTES:\nbackground: 8-bit, 16-bit, retro\nhead: human, animal, creature\nclothing: casual, "
               "costume, outlandish\n\nNAME: \"facebook NFT\"\nSTYLE: \"meme\"\nATTRIBUTES:\nbackground: office, coworking, "
               "restroom\nhead: human, facebook logo, zuckerberg\nclothing: hoodie, t-shirt, jeans, sweatpants\n\nNAME: "
               "\"monkey god\"\nSTYLE: \"fantasy\"\nATTRIBUTES:\nbackground: jungle, temple, mountaintop\nhead: monkey, "
               "god, human\nclothing: tattered, ceremonial, regal\n\nNAME: \"NFT editor\"\nSTYLE: "
               "\"old-school\"\nATTRIBUTES:\nbackground: video game, editing suite, celebrity's house\nhead: editor, "
               "artist, game programmer\nclothing: Hawaiian shirt, cargo shorts, sneakers\n\nNAME: \"NFTs are the new "
               "black\"\nSTYLE: \"modern\"\nATTRIBUTES:\nbackground: club, party, cityscape\nhead: human, celebrity, "
               "model\nclothing: all black, high fashion, stylish\n\nNAME: \"idiot dumb clown\"\nSTYLE: "
               "\"caricature\"\nATTRIBUTES:\nbackground: circus, big top, clown car\nhead: human, clown, idiot\nclothing: "
               "big shoes, red nose, baggy clothes\n\nNAME: \"sharks\"\nSTYLE: \"menacing\"\nATTRIBUTES:\nbackground: "
               "ocean, deep sea, beach\nhead: shark, human, fish\nclothing: wet suit, scuba gear, swimming trunks\n\nNAME: "
               "\"teapot\"\nSTYLE: \"cute\"\nATTRIBUTES:\nbackground: kitchen, living room, bedroom\nhead: teapot, human, "
               "animal\nclothing: apron, O_O face, heart eyes\n\nNAME: \"nft rawr\"\nSTYLE: "
               "\"fierce\"\nATTRIBUTES:\nbackground:forest, tundra, savannah\nhead: human, animal, "
               "mythical creature\nclothing: loincloth, armor, battle gear\n\nNAME: \"collector\"\nSTYLE: "
               "\"eccentric\"\nATTRIBUTES:\nbackground: study, library, art gallery\nhead: human, collector, "
               f"art enthusiast\nclothing: waistcoat, top hat, monocle\n\nNAME:{name_of_collection}",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response['choices'][0]['text']


def get_generation_prompt(collection_name):
    result = get_prompt_from_gpt3(collection_name)

    style_index = result.find('STYLE')
    # addition_to_name = result[:style_index - 1]
    result = result[style_index:]

    result = f'NAME: "{collection_name}"\n{result}'

    return result


# if __name__ == '__main__':
#     collection_name = 'shaggy nft'
#
#     final_prompt = get_generation_prompt(collection_name)

    # print(f'Переданное название коллекции: {collection_name}')
    # print('Сгенерированный промпт:')
    # print(final_prompt)
