{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "app = Flask(__name__)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"regression_DBS_1\")\n",
    "        r1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree_DBS\")\n",
    "        r2 = model2.predict([[rates]])\n",
    "        return(render_template(\"index.html\", result1=r1, result2=r2))\n",
    "    else: \n",
    "        return(render_template(\"index.html\", result1=\"waiting\", result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Aug/2022 13:39:27] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [15/Aug/2022 13:39:27] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:10] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Aug/2022 13:41:18] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:18] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Aug/2022 13:41:21] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Aug/2022 13:41:27] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Aug/2022 13:41:31] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[2022-08-15 13:41:32,310] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\seowk\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-2-c6b193294575>\", line 6, in index\n",
      "    rates = float(request.form.get(\"rates\"))\n",
      "ValueError: could not convert string to float: ''\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:32] \"\u001b[35m\u001b[1mPOST / HTTP/1.1\u001b[0m\" 500 -\n",
      "127.0.0.1 - - [15/Aug/2022 13:41:39] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
