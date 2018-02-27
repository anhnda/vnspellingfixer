import HTMLParser
import optparse

from flask import Flask
from flask import request

from spelling_corrector.general_bare_corrector.corrector import GeneralBareCorrector

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')


spelling_corrector = None

def init_model():
   global spelling_corrector
   spelling_corrector = GeneralBareCorrector()

@app.route('/')
def start():
   #return render_template('index.html')
   return app.send_static_file('index.html')
@app.route('/fix',methods=['GET', 'POST'])
def ner():
   #data = request.data
   sen = request.form['sen']

   sen = HTMLParser.HTMLParser().unescape(sen)
   #sen = sen.decode("utf-8")
   fixed_res,_ = spelling_corrector.fix_general_bigram(sen)
   return fixed_res

if __name__ == '__main__':
   optparser = optparse.OptionParser()
   optparser.add_option(
      "-R", "--port", default="9199",type="int"
   )
   opts = optparser.parse_args()[0]
   port = opts.port

   init_model()


   app.run(debug = False,host='0.0.0.0', port=port)