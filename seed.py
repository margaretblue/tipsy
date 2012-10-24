"""
seed.py
"""
import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
user_id2=model.new_user(db, "louise.s.fox@gmail.com", "yourmom", "Louise")
user_id3=model.new_user(db, "whatdoyouthink@gmail.com", "yeahfool", "HairyMan")
task = model.new_task(db, "Complete this task list", user_id)
task=model.new_task(db, "Feed my dog", user_id2)
task=mode.new_task(db, "somethingsomething", user_id2)
task=mode.new_task(db, "somethingsomething", user_id3)
task=mode.new_task(db, "morestuff", user_id3)