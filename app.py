from urllib import request
from flask import Flask
from flask_ngrok import run_with_ngrok
import requests
app = Flask(__name__)
# run_with_ngrok(app, )
  
@app.route("/")
def hello():
    url = "https://odoo.choicefurnituresuperstore.co.uk/odooAPI/apiOrder_Odoo_To_CFS_FreeStockInsert.php?action=insert_free_stock&operator=Administrator&fId=0&iOrderDetailId=2370183&stockNotes=False&vOrderNo=False&iBrandId=62&brandName=Birlea Furniture&iProductId=105222&vAttribute=False&iQty=1&product_code=WOBS3BSOAK&vCost=114.0&fWhsCode=False&fRMA=False&credit_foc=False&fRemarks=Change Of Mind After Delivery&itemType=freestock&addedBy=Administrator&collection=False&isCollected=False&status=False&eStatus=Active&dDate=2022-02-16 11:18:55"
    result = requests.get(url,allow_redirects = False)
    print(result)
    print(result.json())
    return result.json()
  
if __name__ == "__main__":
  app.run()
