import xml.etree.ElementTree as ET
import secrets

def random_select(list_of_series):
    return secrets.choice(list_of_series)

def anime_url_prep(selected_series_info):
    tmp = list(selected_series_info["series_title"])
    i = 0
    for x in tmp:
        if(tmp[i] == ' ' or tmp[i] == ':'):
            tmp[i] = '_'
        i+=1
    title = "".join(tmp)
    return title

def manga_url_prep(selected_series_info):
    tmp = list(selected_series_info["manga_title"])
    i = 0
    for x in tmp:
        if(tmp[i] == ' ' or tmp[i] == ':'):
            tmp[i] = '_'
        i+=1
    title = "".join(tmp)
    return title

def get_xml():
    xml_name = input("Please enter the name of your exported xml file (make sure to include the .xml): ")
    print("You entered: " + xml_name)
    try:
        mytree = ET.parse(xml_name)
        myroot = mytree.getroot()
        my_info_dictionary = {}
        for x in myroot[0]:
            my_info_dictionary[x.tag] = x.text
    except:
        print("Error: Does not exist. Did not submit a valid xml file")
        quit()
    try:
        if(my_info_dictionary['user_export_type'] == "1"):
            print("Welcome " + my_info_dictionary['user_name'] + ", you have selected an Anime list.\n")
            get_anime(myroot, my_info_dictionary)
        elif(my_info_dictionary['user_export_type'] == "2"):
            print("Welcome " + my_info_dictionary['user_name'] + ", you have selected a Manga list.\n")
            get_manga(myroot, my_info_dictionary)
    except:
        print("Error: Did not submit a valid myanimelist xml file. Requires user_export_type tag in <myinfo>")
        quit()

def get_anime(myroot, my_info_dictionary):

    print("If you are looking to randomize your entire list, enter 1.")
    print("If you are looking to randomize your Completed list, enter 2.")
    print("If you are looking to randomize your Plan to Watch list, enter 3.")
    print("If you are looking to randomize your On-Hold list, enter 4.")
    print("If you are looking to randomize your Dropped list, enter 5.\n")
    status_to_find = input("Which list are you looking to randomize? ")

    if(status_to_find == "1"):
        desired_status = "All"
    elif(status_to_find == "2"):
        desired_status = "Completed"
    elif(status_to_find == "3"):
        desired_status = "Plan to Watch"
    elif(status_to_find == "4"):
        desired_status = "On-Hold"
    elif(status_to_find == "5"):
        desired_status = "Dropped"
    else:
        print("Error: Did not enter a valid input, exiting program, ignore next error message")
        quit()

    print("You have selected your: " + desired_status +" list.\n")
    print("Now randomizing\n")

    list_of_desired_series = []

    if(desired_status == "All"):
        for x in myroot.findall('anime'):
            title=x.find('series_title').text
            list_of_desired_series.append(title)
        
    else:
        if(desired_status == "Completed"):
            for x in myroot.findall('anime'):
                if(x.find('my_status').text == "Completed"):
                    title=x.find('series_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "Plan to Watch"):
            for x in myroot.findall('anime'):
                if(x.find('my_status').text == "Plan to Watch"):
                    title=x.find('series_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "On-Hold"):
            for x in myroot.findall('anime'):
                if(x.find('my_status').text == "On-Hold"):
                    title=x.find('series_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "Dropped"):
            for x in myroot.findall('anime'):
                if(x.find('my_status').text == "Dropped"):
                    title=x.find('series_title').text
                    list_of_desired_series.append(title)

    selected_series = random_select(list_of_desired_series)
    print("Your randomly selected series is: ", selected_series, "\n")
    selected_series_info = {}
    i = 1
    for x in myroot.findall('anime'):
        if(x.find('series_title').text == selected_series):
            for y in myroot[i]:
                selected_series_info[y.tag] = y.text
            break
        else:
            i+=1
            continue

    url = "myanimelist.net/anime/"
    title = anime_url_prep(selected_series_info)
    url = url + selected_series_info["series_animedb_id"] + '/' + title
    print("{}: {}".format("series_title", selected_series_info["series_title"]))
    print("{}: {}".format("myanimelist_url", url))
    print("{}: {}".format("series_type", selected_series_info["series_type"]))
    print("{}: {}".format("series_episodes", selected_series_info["series_episodes"]))
    print("{}: {}".format("my_watched_episodes", selected_series_info["my_watched_episodes"]))
    print("{}: {}".format("my_score", selected_series_info["my_score"]))
    print("{}: {}\n".format("my_status", selected_series_info["my_status"]))

def get_manga(myroot, my_info_dictionary):
    print("If you are looking to randomize your entire list, enter 1.")
    print("If you are looking to randomize your Completed list, enter 2.")
    print("If you are looking to randomize your Plan to Read list, enter 3.")
    print("If you are looking to randomize your On-Hold list, enter 4.")
    print("If you are looking to randomize your Dropped list, enter 5.\n")
    status_to_find = input("Which list are you looking to randomize? ")

    if(status_to_find == "1"):
        desired_status = "All"
    elif(status_to_find == "2"):
        desired_status = "Completed"
    elif(status_to_find == "3"):
        desired_status = "Plan to Read"
    elif(status_to_find == "4"):
        desired_status = "On-Hold"
    elif(status_to_find == "5"):
        desired_status = "Dropped"
    else:
        print("Error: Did not enter a valid input, exiting program, ignore next error message")
        quit()

    print("You have selected your: " + desired_status +" list.\n")
    print("Now randomizing\n")

    list_of_desired_series = []

    if(desired_status == "All"):
        for x in myroot.findall('manga'):
            title=x.find('manga_title').text
            list_of_desired_series.append(title)
    else:   
        if(desired_status == "Completed"):
            for x in myroot.findall('manga'):
                if(x.find('my_status').text == "Completed"):
                    title=x.find('manga_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "Plan to Read"):
            for x in myroot.findall('manga'):
                if(x.find('my_status').text == "Plan to Read"):
                    title=x.find('manga_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "On-Hold"):
            for x in myroot.findall('manga'):
                if(x.find('my_status').text == "On-Hold"):
                    title=x.find('manga_title').text
                    list_of_desired_series.append(title)
        elif(desired_status == "Dropped"):
            for x in myroot.findall('manga'):
                if(x.find('my_status').text == "Dropped"):
                    title=x.find('manga_title').text
                    list_of_desired_series.append(title)

    selected_series = random_select(list_of_desired_series)
    print("Your randomly selected series is: ", selected_series, "\n")
    selected_series_info = {}
    i = 1            
    for x in myroot.findall('manga'):
        if(x.find('manga_title').text == selected_series):
            for y in myroot[i]:
                selected_series_info[y.tag] = y.text
            break
        else:
            i+=1
            continue

    url = "myanimelist.net/manga/"
    title = manga_url_prep(selected_series_info)
    url = url + selected_series_info["manga_mangadb_id"] + '/' + title
    print("{}: {}".format("manga_title", selected_series_info["manga_title"]))
    print("{}: {}".format("myanimelist_url", url))
    print("{}: {}".format("manga_volumes", selected_series_info["manga_volumes"]))
    print("{}: {}".format("manga_chapters", selected_series_info["manga_chapters"]))
    print("{}: {}".format("my_read_volumes", selected_series_info["my_read_volumes"]))
    print("{}: {}".format("my_read_chapters", selected_series_info["my_read_chapters"]))
    print("{}: {}".format("my_score", selected_series_info["my_score"]))
    print("{}: {}\n".format("my_status", selected_series_info["my_status"]))

if __name__ == '__main__':
    print("Welcome to the MyAnimeList list randomizer!\n")
    print("This app will randomly select a series from either your anime/manga list exported from MyAnimelist so you will no longer have to decide what to watch/read. Leave it all to rng!\n")
    print("To get started, just export one of your lists from your MyAnimeList account and place it in the location of this app.\n")
    get_xml()