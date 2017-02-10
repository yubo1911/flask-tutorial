export FLASK_APP=hello.py
flask run
or
python -m flask run

(trust all the network users or disable debugger)
flask run --host=0.0.0.0

to auto reload source changes, use
export FLASK_DEBUG=1
