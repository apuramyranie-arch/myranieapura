import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
