#-*-coding:utf-8-*-


class Blog:
    def __init__(self):
        """
        state:
            1 : header
            2 : body
            3 : other
        """
        self.load_state = 1
        self.article_list = []
        self.article = Article()

    def load(self, path):
        with open(path, 'r') as f:
            for row in f:
                self.parse_row(row)

    def export(self, path):
        pass

    def parse_row(self, row):
        if '--------\n' in row:
            self.next_article()
        elif '-----\n' in row:
            self.next_state()
        elif self.load_state == 1:
            self.article.add_header(row)
        elif self.load_state == 2:
            self.article.add_body(row)

    def next_article(self):
        self.article_list.append(self.article)
        self.article = Article()
        self.load_state = 1

    def next_state(self):
        self.load_state += 1

    def reset_all_article_category(self):
        for article in self.article_list:
            article.reset_category()

    def set_all_article_category(self, category):
        for article in self.article_list:
            article.set_category(category)

    def get_all_category(self):
        my_category_set = set()
        for article in self.article_list:
            for category in article.category:
                my_category_set.add(category)

        return my_category_set

    def try_paste_category(self, category):
        for article in self.article_list:
            article.try_paste_category(category)

    def get_no_category_article(self):
        return [ 
            article for article in self.article_list 
            if len(article.category) == 0
        ]
    
    def export(self, path):
        for article in self.article_list:
            article.export(path)

class Article:
    def __init__(self):
        self.author = 'mtb_beta'
        self.body = ''
        self.title = ''
        self.basename = ''
        self.status = 'Draft'
        self.allow_comments = '1'
        self.convert_breaks = '0'
        self.date = ''
        self.category = set()
        self.image = ''

    def add_header(self, row):
        row = row.replace('\n', '')
        key, value= row.split(':', 1)
        value = value[1:]
        if key == "AUTHOR":
            self.author = value
        elif key == "TITLE":
            self.title = value
        elif key == 'BASENAME':
            self.basename = value
        elif key == 'STATUS':
            self.status = value
        elif key == 'ALLOW COMMENTS':
            self.allow_comments = value
        elif key == 'CONVERT BREAKS':
            self.convert_breaks = value
        elif key == 'DATE':
            self.date = value
        elif key == 'CATEGORY':
            self.category.add(value)
        elif key == 'IMAGE':
            self.image = value
        else:
            print('warning:skipped row.{}'.format(row))

    def add_body(self, row):
        if 'BODY' in row:
            pass
        else:
            self.body += row

    def reset_category(self):
        self.category = set()

    def set_category(self, category):
        self.category.add(category)
    
    def try_paste_category(self, category):
        if category in self.title or category in self.body:
            self.category.add(category)
