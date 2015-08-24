import fresh_tomatoes
import media
import operator

fantastic_four = media.Movie("Fantastic Four",
                            "The team must learn to harness abilities gained from an alternate universe to save Earth from a friend turned enemy",
                            "https://upload.wikimedia.org/wikipedia/en/f/f4/Fantastic_Four_2015_poster.jpg",
                            "https://www.youtube.com/watch?v=_rRoD28-WgU",
                            2015)

avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron",
                                      "The Avengers must work together to defeat Ultron, a mechanical artificial intelligence bent on human extinction",
                                      "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                                      "https://www.youtube.com/watch?v=tmeOjFno6Do",
                                      2015)

ant_man = media.Movie("Ant-Man",
                      "Lang must help defend Dr. Pym's Ant-Man technology and plot a heist with worldwide ramifications",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                      "https://www.youtube.com/watch?v=pWdKf3MneyI",
                      2015)

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                       "Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact",
                                       "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                                       "https://www.youtube.com/watch?v=2XltzyLcu0g",
                                       2014)

x_men_days_of_future_past = media.Movie("X-Men: Days of Future Past",
                                        "Wolverine traveling back in time to 1973 to save the future of mankind",
                                        "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                                        "https://www.youtube.com/watch?v=pK2zYHWDZKo",
                                        2014)

the_amazing_spider_man_2 = media.Movie("The Amazing Spider-Man 2",
                                       "Sequel to The Amazing Spider-Man",
                                       "https://upload.wikimedia.org/wikipedia/en/0/02/The_Amazing_Spiderman_2_poster.jpg",
                                       "https://www.youtube.com/watch?v=DlM2CWNTQ84",
                                       2014)

captain_america_the_winter_soldier = media.Movie("Captain America: The Winter Soldier",
                                                  "Captain America, Black Widow, and Falcon join forces to uncover a conspiracy within S.H.I.E.L.D. while facing a mysterious assassin known as the Winter Soldier",
                                                  "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
                                                  "https://www.youtube.com/watch?v=7SlILk2WMTI",
                                                  2014)

the_wolverine = media.Movie("The Wolverine",
                            "Logan travels to Japan, where he engages an old acquaintance in a struggle that has lasting consequences",
                            "https://upload.wikimedia.org/wikipedia/en/7/74/The_Wolverine_posterUS.jpg",
                            "https://www.youtube.com/watch?v=Rh1LdTFkm7I",
                            2013)

iron_man_3 = media.Movie("Iron Man 3",
                         "Tony Stark tries to recover from posttraumatic stress disorder caused by the events of The Avengers, while investigating a terrorist organization led by the mysterious Mandarin",
                         "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=2CzoSeClcw0",
                         2013)

thor_the_dark_world = media.Movie("Thor: The Dark World",
                                  "Thor teams up with Loki to save the Nine Realms from the Dark Elves led by the vengeful Malekith, who intends to plunge the universe into darkness",
                                  "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
                                  "https://www.youtube.com/watch?v=npvJ9FTgZbM",
                                  2013)

the_avengers = media.Movie("The Avengers",
                           "Nick Fury, director of the peacekeeping organization S.H.I.E.L.D., recruits Iron Man, Captain America, the Hulk, and Thor to form a team that must stop Thor's brother Loki",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                           2012)

the_amazing_spider_man = media.Movie("The Amazing Spider-Man",
                                     "Parker must stop Dr. Curt Connors as a mutated lizard from spreading a mutation serum to the city's human population",
                                     "https://upload.wikimedia.org/wikipedia/en/0/02/The_Amazing_Spider-Man_theatrical_poster.jpeg",
                                     "https://www.youtube.com/watch?v=oX9ZT3RbYE4",
                                     2012)

man_of_steel = media.Movie("Man of Steel",
                           "a reboot of the Superman film series that portrays the character's origin story",
                           "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                           "https://www.youtube.com/watch?v=T6DJcgm3wNY",
                           2013)

the_dark_knight_rises = media.Movie("The Dark Knight Rises",
                                    "Bane (Tom Hardy), a revolutionary bent on destroying Gotham City who forces an older Bruce Wayne to come out of retirement and become Batman again",
                                    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                                    "https://www.youtube.com/watch?v=GokKUqLcvD8",
                                    2012)

green_lantern = media.Movie("Green Lantern",
                            "Hal is given a ring that grants him superpowers and must confront the evil Parallax, who threatens to upset the balance of power in the universe",
                            "https://upload.wikimedia.org/wikipedia/en/6/6b/Green_Lantern_poster.jpg",
                            "https://www.youtube.com/watch?v=f8ZPg8uaoR0",
                            2011)

#List of Marvel movies
marvel_movies = [fantastic_four, ant_man, avengers_age_of_ultron,
            guardians_of_the_galaxy, x_men_days_of_future_past, the_amazing_spider_man_2, captain_america_the_winter_soldier,
            thor_the_dark_world, the_wolverine, iron_man_3,
            the_amazing_spider_man, the_avengers]

#List of DC movies
dc_movies = [man_of_steel,
            the_dark_knight_rises,
            green_lantern]

#List of Marvel and DC movies
movies = marvel_movies + dc_movies

#Sort movies by year of release in descending order
sorted_movies = sorted(movies, key=operator.attrgetter('year'), reverse=True)

fresh_tomatoes.open_movies_page(sorted_movies)
