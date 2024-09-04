pozdrav = "budte zdravi"


if pozdrav == "budte zdravi":
    print("Ahoj")
elif pozdrav == "budte zdrava":
    print("budte zdrava")




match pozdrav:
    case "budte zdravi":
        print("budte zdravi")
    case "budte zdrava":
        print("budte zdrava")
    case "budte zdraveni":
        print("budte zdraveni")