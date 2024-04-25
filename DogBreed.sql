PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE compatibility (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    with_other_pets BOOLEAN,
    with_children BOOLEAN,
    with_seniors BOOLEAN,
    lifestyle_type VARCHAR(50) NOT NULL
);
INSERT INTO compatibility VALUES(NULL,'Bulldog',0,1,0,'affectionate');
INSERT INTO compatibility VALUES(NULL,'Boxer',1,1,1,'affectionate');
INSERT INTO compatibility VALUES(NULL,'German Shepard',0,1,1,'very affectionate');
INSERT INTO compatibility VALUES(NULL,'Labrador Retriever',1,1,1,'extremely affectionate');
INSERT INTO compatibility VALUES(NULL,'Chow Chow',0,0,0,'not very affectionate');
INSERT INTO compatibility VALUES(NULL,'Border Collie',1,1,0,'extremely affectionate');
CREATE TABLE adaptability (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    temperament VARCHAR(255),
    adjustment VARCHAR(255),
    sociability VARCHAR(255)
);
INSERT INTO adaptability VALUES(NULL,'Bulldog','somewhat adaptable','very hard to adjust','sociable');
INSERT INTO adaptability VALUES(NULL,'Boxer','sensitive','somewhat adaptable','very social');
INSERT INTO adaptability VALUES(NULL,'German Shepard','very sensitive','adaptable','sociable');
INSERT INTO adaptability VALUES(NULL,'Labrador Retriever','very sensitive','somewhat adaptable','very sociable');
INSERT INTO adaptability VALUES(NULL,'Chow Chow','not sensitive','somewhat adaptable','not at sociable');
INSERT INTO adaptability VALUES(NULL,'Border Collie','very sensitive','somewhat adaptable','sociable');
CREATE TABLE grooming (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    frequency VARCHAR(100),
    shedding_level VARCHAR(100),
    coat_type VARCHAR(100)
);
INSERT INTO grooming VALUES(NULL,'Pomeranian','4-6 weeks','moderate','double');
INSERT INTO grooming VALUES(NULL,'Bulldog','once a week','moderate','short');
INSERT INTO grooming VALUES(NULL,'Boxer','once a week','moderate','short');
INSERT INTO grooming VALUES(NULL,'German Sheperd','few times a week','heavy','double');
INSERT INTO grooming VALUES(NULL,'Labrador Retriever','few times a week','heavy','short, dense double[D[');
INSERT INTO grooming VALUES(NULL,'Chow Chow','daily','heavy','thick, double');
INSERT INTO grooming VALUES(NULL,'Border Collie','daily','moderate','medium, double');
CREATE TABLE health (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    lifespan VARCHAR(100),
    health_issues VARCHAR(255),
    genetic_disposition VARCHAR(255)
);
INSERT INTO health VALUES(NULL,'Bulldog','10-15 years','skin allergies, hip dysplasia, elbow dysplasia','cherry eye, breathing issues');
INSERT INTO health VALUES(NULL,'Boxer','10-12 years','skin allergies, eye problems, bloating issues','respiratory issues');
INSERT INTO health VALUES(NULL,'German Sheperd','9-13 years','hip dysplasia, myelopathy, bloating issues, pancreatitis','allergies, panosteitis');
INSERT INTO health VALUES(NULL,'Labrador Retriever','10-12 years','hip dysplasia, ear infections, obesity','progressive retinal atrophy, exercise-induced collapse');
INSERT INTO health VALUES(NULL,'Chow Chow','9-15 years','dysplasia, entropion, glaucoma','skin issues, thyroid disorders, bloating issues, heart issues');
INSERT INTO health VALUES(NULL,'Border Collie','12-15 years','dysplasia','allergies, progressive retinal atrophy, epilepsy, deafness');
CREATE TABLE exercise_needs (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    mental_stimulation VARCHAR(100),
    exercise_requirements VARCHAR(100),
    activity_level VARCHAR(100),
    suitability VARCHAR(100)
);
INSERT INTO exercise_needs VALUES(NULL,'Bulldog','active','moderate','moderate','very suitable');
INSERT INTO exercise_needs VALUES(NULL,'Boxer','active','regularly','high','energetic and playful');
INSERT INTO exercise_needs VALUES(NULL,'German Sheperd','highly active','regularly','high','athletic');
INSERT INTO exercise_needs VALUES(NULL,'Labrador Retriever','very active','substantial','high','athletic and playful');
INSERT INTO exercise_needs VALUES(NULL,'Chow Chow','active','moderate','moderate','calm and independent');
INSERT INTO exercise_needs VALUES(NULL,'Border Collie','very acive','regularly','very high','energetic');
CREATE TABLE appearance (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    physical_features TEXT,
    breed_standards TEXT,
    size VARCHAR(50),
    color VARCHAR(100)
);
INSERT INTO appearance VALUES(NULL,'Bulldog','muscular build, wrinkled face, short muzzle, underbite','large head, rose-shaped ears, short body, short coat','medium','white');
INSERT INTO appearance VALUES(NULL,'Boxer','muscular build, square head, brachycephalic muzzle, docked tail','broad head, dark eyes, short muzzle, muscular neck, , compact body','large','fawn');
INSERT INTO appearance VALUES(NULL,'German Sheperd','muscular build, long muzzle, upright ears, bushy tail','proportioned body, straight back, broad skull','large','black and tan');
INSERT INTO appearance VALUES(NULL,'Labrador Retreiver','muscular build, broad head, pendant eears, otter tail','medium muzzle, strong back, deep chest, broad head','medium-large','yellow, black, chocolate');
INSERT INTO appearance VALUES(NULL,'Chow Chow','compact body, large head, short muzzle, triangular ears','flat head, almond eyes, broad chest, straight legs, high and curled tail','medium','red, black, cinnamon, cream');
INSERT INTO appearance VALUES(NULL,'Border Collie','strong body, moderate muzzle, triangular ears, low tail','broad skull, oval eyes, straight back, deep chest','medium','white, brown');
CREATE TABLE trainability (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(100) NOT NULL,
    intelligence_level VARCHAR(100),
    trainability_rating VARCHAR(100),
    training_methods TEXT
);
INSERT INTO trainability VALUES(NULL,'Bulldog','basic','moderate','positive reinforcement');
INSERT INTO trainability VALUES(NULL,'Boxer','very intelligent','exceptional','motivation');
INSERT INTO trainability VALUES(NULL,'German Sheperd','exceptional','exceptional','motivation');
INSERT INTO trainability VALUES(NULL,'Labrador Retriever','very intelligent','exceptional','positive reinforcement');
INSERT INTO trainability VALUES(NULL,'Chow Chow','moderate','low','rewarding');
INSERT INTO trainability VALUES(NULL,'Border Collie','intelligent','highly trainable','rewarding');
COMMIT;
