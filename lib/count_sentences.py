#!/usr/bin/env python3

class MyString:
      
      def __init__(self, value=""):
            self._value = value
      
      def get_value(self):
            return self._value
      
      def set_value(self, given_val):
            if(type(given_val)==str):
                  self._value = given_val
            else:
                  print("The value must be a string.")

      value = property(get_value, set_value)

      def is_sentence(self):
           return self._value.endswith(".")
      def is_question(self):
           return self._value.endswith("?")
      def is_exclamation(self):
           return self._value.endswith("!")

      def count_sentences(self):
          given_sentence = self.value
          for punc in ["?", "!"]:
               given_sentence = given_sentence.replace(punc, ".")
               print(given_sentence)
          sentences = [s for s in given_sentence.split(".") if s]

          print(len(sentences))
          return len(sentences)

          #  stringArr in self.value
          #  print len(string)

new_str = MyString()
new_str.value = "hello? yes!"
new_str.count_sentences()