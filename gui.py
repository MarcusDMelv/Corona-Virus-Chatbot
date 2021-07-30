import random

from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.storage.storage_adapter import StorageAdapter
from chatterbot.tagging import PosHypernymTagger
from chatterbot.tokenizers import get_sentence_tokenizer
from chatterbot.corpus import load_corpus, list_corpus_files
from chatterbot.trainers import ChatterBotCorpusTrainer

import tkinter as tk

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            "GUI Bot",
            # response_selection_method=get_random_response,
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            database_uri="sqlite:///database.sqlite3"
        )

        corpus = ChatterBotCorpusTrainer(self.chatbot)

        corpus.train(
            'chatterbot.corpus.custom.CoronaVirus'

        )

        # title
        self.title("Coronavirus Chatbot")
        # Gui
        self.initialize()

    # function for GUI
    def initialize(self):
        """
        Set window layout.
        """

        self.grid()
        # color
        self.configure(bg='purple')
        # create enter button for user
        self.respond = ttk.Button(self, text='Bot reply to:', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)
        # generate from randomize list about Facts
        self.respond = ttk.Button(self, text='Coronavirus Facts', command=self.get_coronavirus_facts)
        self.respond.grid(column=1, row=3, sticky='nesw', padx=3, pady=3)
        # generate from randomize list about Facts
        self.respond = ttk.Button(self, text='Coronavirus Rumors', command=self.get_coronavirus_rumors)
        self.respond.grid(column=0, row=3, sticky='nesw', padx=3, pady=3)
        # generate from randomize list about Facts
        self.respond = ttk.Button(self, text='How to Fight!', command=self.get_coronavirus_fight)
        self.respond.grid(column=1, row=4, sticky='nesw', padx=3, pady=3)
        # generate from randomize list about Facts
        self.respond = ttk.Button(self, text='Nicknames', command=self.get_coronavirus_nicknames)
        self.respond.grid(column=0, row=4, sticky='nesw', padx=3, pady=3)
        # users entry input for the bot
        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
        # conversation label for scrolledtext box
        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)
        # entry for user and bot conversation.
        self.conversation = ScrolledText.ScrolledText(self, width=50, wrap=tk.WORD, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)
        # able scrolledtext to be edit
        self.conversation['state'] = 'normal'
        # insert directions on Chatbot
        self.conversation.insert(
            tk.END, "PLEASE READ!!\n"
                    "\n"
                    "About: This chatbot is very informational about the Coronavirus!\n"
                    "\n"
                    "       -Either type with the bot and press 'CHAT'\n"
                    "                            OR:"
                    " \n"
                    "      -Select a CATEGORY from the bottom to get more specific information\n"
                    "\n"
                    "Chat: Would you like to talk about the Coronavirus?\n"
                    "\n"
                    "Rumors: Too much fake news!\n"
                    "\n"
                    "Facts: Quick facts about the Coronavirus!\n"
                    "\n"
                    "Nicknames: Be careful with these nicknames some people may find them offensive!\n"
                    "\n"
                    "How to Fight: We can fight the virus together!\n"
                    "\n"
                    ""

        )
        # disable scrolltext
        self.conversation['state'] = 'disabled'

    # delete entries in scrolledtext
    def delete_convo(self):
        # allows scrolltext box to be edit
        self.conversation['state'] = 'normal'
        # erases last input
        self.conversation.delete('1.0', tk.END)
        # scrolledtext can not be edit
        self.conversation['state'] = 'disabled'

    # bot response to user
    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        # deletes last statements by bot bot and user
        self.delete_convo()
        # users input
        user_input = self.usr_input.get()
        # when user press enter
        # delete text
        self.usr_input.delete(0, tk.END)
        time.sleep(0.3)
        # output response according to user input
        response = self.chatbot.get_response(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "You: " + user_input + "\n" + "\n" + f"Bot: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)

    # facts_list
    def get_coronavirus_facts(self):
        self.delete_convo()
        # list created
        self.conversation.delete('1.0', tk.END)
        coronavirus = [f'Coronavirus disease 2019 (COVID-19) is a respiratory illness \nthat can spread from person to '
                       'person.\n', 'The virus that causes COVID-19 is a novel coronavirus that was first identified '
                                    f'during an investigation into an outbreak in Wuhan, China. \n', f"Risk of "
                                                                                                     f"infection is "
                                                                                                     f"higher if you "
                                                                                                     f"come close "
                                                                                                     f"with someone "
                                                                                                     f"who is "
                                                                                                     f"    carrying the "
                                                                                                     f"virus\n",
                       "The virus that causes COVID-19 probably emerged from ananimal source, but is now spreading from person to person. \n",
                       " It also may be possible that a person can get COVID-19 by touching a surface or object that hasthe virus on it and then touching their own mouth,   nose, or possibly their eyes.\n",
                       "Some patients have pneumonia in both lungs, multi-organ failure and in some cases death.\n",
                       "There is currently no vaccine to protect against COVID-19. \n",
                       "tight-fitting respirators (such as the N95) can protect health care workers as they care for infected patients. For the general public without      respiratory illness, wearing lightweight disposable surgical masks is not       recommended Because they don’t fit tightly. \n",
                       "The symptoms of most coronaviruses are similar to those of a common cold, including sneezing, stuffy or runny nose, sore throat, coughing, watery   eyes, mild headache and mild body aches.\n",
                       "\n"]
        # list will be randomized
        random_facts = random.choice(coronavirus)
        # delete last input by user
        self.usr_input.delete(0, tk.END)
        # response will be random
        response = random_facts
        # scrolledtext is able to be edit
        self.conversation['state'] = 'normal'
        # insert response from list in to scrolled text
        self.conversation.insert(
            tk.END, "Quick Fact: " + str(response) + "\n"
        )
        # scrolledtext can't be edit
        self.conversation['state'] = 'disabled'
        time.sleep(0.5)

    # rumor_list
    def get_coronavirus_rumors(self):
        self.delete_convo()
        # list created
        coronavirus = [" Older people are more susceptible\n",
                       "Is it dangerous to eat at a Chinese restaurant or to receive a package from China?\n",
                       "Eating garlic or Vitamin C helps keep the virus away?\n",
                       "Wearing more than one mask will help prevent infection\n",
                       "Spraying chlorine or alcohol on skin kills viruses in the body\n",
                       "Children cannot catch COVID-19\n",
                       "COVID-19 is just like the flu\n", " Cats and dogs spread coronavirus\n",
                       "The virus will die off when temperatures rise in the spring\n",
                       "Flu and pneumonia vaccines protect against COVID-19\n",
                       ]
        # list will be randomized
        random_facts = random.choice(coronavirus)
        self.usr_input.delete(0, tk.END)
        # ai will spit out list
        response = random_facts
        # scrolltext box opens up to be edited
        self.conversation['state'] = 'normal'
        # input statements in scrolledtext box
        self.conversation.insert(
            tk.END, "Rumor:" + str(response) + "\n"
        )
        # disable box
        self.conversation['state'] = 'disabled'
        # rest
        time.sleep(0.5)

    # fight_coronavirus
    def get_coronavirus_fight(self):
        self.delete_convo()
        # list with specific rumors
        coronavirus = [" Washing your hands for 20 sec!\n", "\n"]
        # list will be randomized
        random_facts = random.choice(coronavirus)
        self.usr_input.delete(0, tk.END)
        # ai will spit out list
        response = random_facts
        # scrolltext box opens up to be edited
        self.conversation['state'] = 'normal'
        # input statements in scrolledtext box
        self.conversation.insert(
            tk.END, "Lets fight by: " + str(response) + "\n"
        )
        # disable box
        self.conversation['state'] = 'disabled'
        # rest
        time.sleep(0.5)
    # nicknames_list
    def get_coronavirus_nicknames(self):
        self.delete_convo()
        # list with specific rumors
        coronavirus = ["'Kung-Flu'\n", "'Wuhan Coronavirus'\n",
                       "'These nicknames for the virus can be seen as offensive'\n",
                       "'The Chinese virus'\n", "'Wuhan Coronavirus'\n", ]
        # list will be randomized
        random_facts = random.choice(coronavirus)
        self.usr_input.delete(0, tk.END)
        # ai will spit out list
        response = random_facts
        # scrolltext box opens up to be edited
        self.conversation['state'] = 'normal'
        # input statements in scrolledtext box
        self.conversation.insert(
            tk.END, "Nickname: " + str(response) + "\n"
        )
        # disable box
        self.conversation['state'] = 'disabled'
        # rest
        time.sleep(0.5)


gui_example = TkinterGUIExample()
gui_example.mainloop()
