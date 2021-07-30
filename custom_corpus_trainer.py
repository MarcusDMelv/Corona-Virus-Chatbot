from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot, filters
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import StorageAdapter

chatbot = ChatBot('Charlie', response_selection_method=get_most_frequent_response,
                  # bot will try not to repeat responses to the user
                  # filters=[filters.get_recent_repeated_responses],
                  # SQL storage_adapters
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  # database
                  database_uri='sqlite:///database.sqlite3',
                  # logic adapters
                  # best_match
                  # default_response
                  logic_adapters=[
                      {
                          # using best match
                          'import_path': 'chatterbot.logic.BestMatch',
                          # default response ( low confidence )
                          'default_response': 'I am sorry, but I do not understand.',
                          # if data is 90% similar they will be clustered together
                          'maximum_similarity_threshold': 0.90,
                          "response_selection_method": "chatterbot.response_selection.get_first_response",
                      }
                  ],
                  # modify users input
                  # removes any extra white space
                  # cleans html characters
                  preprocessors=[
                      # removes any extra whitespaces
                      'chatterbot.preprocessors.clean_whitespace',
                      # Convert escaped html characters into unescaped html characters. For example: “&lt;b&gt;”
                      # becomes “<b>”.
                      'chatterbot.preprocessors.unescape_html'
                  ],
                  #  A filter that eliminates possibly repetitive responses to prevent
                  #     a chat bot from repeating statements that it has recently said.

                  )

corpus = ChatterBotCorpusTrainer(chatbot)

corpus.train(
    'chatterbot.corpus.custom.CoronaVirus'

)
