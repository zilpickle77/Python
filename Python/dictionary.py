eyecolor={
    "Kenji Kishimoto" : "brown",
    "Marie" : "green",
    "Jack Harlow" : "blue"
}
print(eyecolor["Kenji Kishimoto"])
#prints brown
print(eyecolor["Marie"])
#prints green
print(eyecolor["Jack Harlow"])
#prints blue
eyecolor.pop("Marie")
print(eyecolor)
eyecolor["Aaron Warner"] = "green"
print(eyecolor)