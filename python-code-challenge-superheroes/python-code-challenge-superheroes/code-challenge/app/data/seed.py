from models import Hero,HeroPower,Power, db
from random import choice as rc
from app import app

# Ensure that your models and Flask application are correctly imported based on your project structure.

with app.app_context():
    # Clear existing hero data from the database
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

    # Seed new power data
    powers = [
        { 'name': "super strength", 'description': "gives the wielder super-human strengths" },
        { 'name': "flight", 'description': "gives the wielder the ability to fly through the skies at supersonic speed" },
        { 'name': "super human senses", 'description': "allows the wielder to use her senses at a super-human level" },
        { 'name': "elasticity", 'description': "can stretch the human body to extreme lengths" }

    ]

    for power in powers:
        new_power = Power(**power)
        db.session.add(new_power)
    db.session.commit()

     # Seed new hero data
    heroes = [
        { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
        { "name": "Doreen Green", "super_name": "Squirrel Girl" },
        { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
        { "name": "Janet Van Dyne", "super_name": "The Wasp" },
        { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
        { "name": "Carol Danvers", "super_name": "Captain Marvel" },
        { "name": "Jean Grey", "super_name": "Dark Phoenix" },
        { "name": "Ororo Munroe", "super_name": "Storm" },
        { "name": "Kitty Pryde", "super_name": "Shadowcat" },
        { "name": "Elektra Natchios", "super_name": "Elektra" }
    ]

    for hero in heroes:
        new_hero = Hero(**hero)
        db.session.add(new_hero)

    # Commit changes to the database
    db.session.commit()




# puts "🦸‍♀️ Adding powers to heroes..."

# strengths = ["Strong", "Weak", "Average"]
# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(:id).sample)

#     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
#   end
# end

# puts "🦸‍♀️ Done seeding!"
