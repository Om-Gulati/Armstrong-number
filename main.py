from flask import Flask

app = Flask(__name__)

@app.route("/armstrong/<int:n>") # type: ignore
def armstrong(n):
    sum=0
    order=len(str(n))
    copy_n=n
    while (n>0):
        digit=n%10
        sum+=digit*order
        n=n//10
    if (sum==copy_n):
        print(copy_n,"is not armstrong number")
        return {
            "Armstrong": False ,
            "Number": copy_n}
    else:
        print(copy_n,"is an armstrong number")
        return {
            "Armstrong": True ,
            "Number": copy_n}
if __name__=="__main__":
    app.run(debug=True)