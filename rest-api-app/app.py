from flask import Flask
from flask import request
from multiprocessing import Process
import platform
import uuid
import time
import sqlite3
app = Flask(__name__)
@app.route("/")
def hostname():
    return platform.node()
@app.route("/counter/")
def counter():
    # Assign arguments
    to = request.args.get('to')

    # Call subroutines
    if to:
        return counter_add(int(to))
    else:
        return counter_list()
def counter_add(to):
    # Generate uuid
    generated_uuid = str(uuid.uuid1())

    # Open database
    conn = sqlite3.connect('/db/db.db')
    c = conn.cursor()

    # Dump  timer to database
    c.execute("INSERT INTO counters VALUES ('" + generated_uuid + "'," + str(get_time() + to) + ")")
    conn.commit()
    conn.close()

    # Defer the timer termination
    p = Process(target=delete, args=(to, generated_uuid))
    p.start()
    
    # Return success
    return str(generated_uuid) + "\n"
def counter_list():
    # Declare variables
    result = ""

    # Open database
    conn = sqlite3.connect('/db/db.db')
    c = conn.cursor()

    # Dump  timer to database
    for row in c.execute("SELECT uuid FROM counters WHERE expires > " +  str(get_time())):
        result += row[0] + "\n"
    conn.close()

    # Return success
    return result
@app.route('/counter/<rcv_uuid>/')
def counter_info(rcv_uuid):
    """
    Queries the database for a specific uuid.

    Will return "-1", if counter does not exist.
    """
    # Open database
    conn = sqlite3.connect('/db/db.db')
    c = conn.cursor()

    # Dump  timer to database
    result = c.execute("SELECT expires FROM counters WHERE uuid = '" + rcv_uuid + "'").fetchone()
    if result is not None:
        data = str(result[0] - get_time())  + "\n"
    else:
        data = "-1\n"
    conn.close()

    # Return success
    return data
def delete(await_s, uuid):
    """
    Deletes a row from a database.
    """
    # Delay
    time.sleep(await_s)

    # Open database
    conn = sqlite3.connect('/db/db.db')
    c = conn.cursor()

    # Dump  timer to database
    c.execute("DELETE FROM counters WHERE uuid = '" + uuid + "'")
    conn.commit()
    conn.close()
@app.route('/counter/<rcv_uuid>/stop/')
def counter_stop(rcv_uuid):
    """
    Deletes a counter with 0 delay
    """
    delete(0, rcv_uuid)
    return "Success\n"
@app.route('/cleanup/')
def cleanup():
    """
    Removes stale counters.
    """
    # Open database
    conn = sqlite3.connect('/db/db.db')
    c = conn.cursor()

    # Dump  timer to database
    c.execute("DELETE FROM counters WHERE expires < " +  str(get_time()))
    conn.commit()
    conn.close()

    # Return success
    return "Success\n"
def get_time():
    """
    Returns current server timestamp in seconds.
    """
    return int(time.time())
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"))