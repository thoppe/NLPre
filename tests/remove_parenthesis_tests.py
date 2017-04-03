from nose.tools import *
from nlpre import remove_parenthesis


class Remove_Parenthesis_Tests():
    def __init__(self):
        self.remove = remove_parenthesis()

    #def single_parenthesis_pair_test(self):
    #    doc = 'hello (world) world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def single_brackets_pair_test(self):
    #    doc = 'hello [world] world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def single_curly_pair_test(self):
    #    doc = 'hello {world} world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def multiple_brackets_pair_test(self):
    #    doc = 'hello [[world] world] world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def multiple_curly_pair_test(self):
    #    doc = 'hello {{world} world} world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def multiple_parenthesis_pair_test(self):
    #    doc = 'hello ((world) world) world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)
    def multiple_parenthesis_pair_test(self):
        doc = 'Ad Ba Ca (Da Ed Ff (Ga Ha) In) Jo. Ka Le'
        doc_right = 'A B C J.\n K L'
        doc_new = self.remove(doc)

        assert_equals(doc_right, doc_new)

            #def single_parenthesis_test(self):
    #    doc = 'hello (world world'
    #    doc_right = 'hello world world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def single_bracket_test(self):
    #    doc = 'hello [world world'
    #    doc_right = 'hello world world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def single_curly_test(self):
    #    doc = 'hello {world world'
    #    doc_right = 'hello world world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def unbalanced_parenthesis_test(self):
    #    doc = 'hello (((world) world) world'
    #    doc_right = 'hello world world world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    # Code doesn't account for multiple sentences within a parenthesis
    # I'm not sure when this case will be encountered, unless we're parsing DFW novels
    #def multisentence_paranthesis_test(self):
    #    doc = 'hello (world. Goodnight moon) world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    #def multisentence_bracket_test(self):
    #    doc = 'hello [world. Goodnight moon] world'
    #    doc_right = 'hello world'
    #    doc_new = self.remove(doc)

    #    assert_equals(doc_right, doc_new)

    def multisentence_curly_test(self):
        doc = 'hello {world. Goodnight moon} world'
        doc_right = 'hello world'
        doc_new = self.remove(doc)

        assert_equals(doc_right, doc_new)
