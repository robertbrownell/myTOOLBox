# =====================================================================================#  to Import this write      import mytoolbox
# =---   ___                                   _       __  __             _        ---=#  then   mytoolbox.red("Is this Red?")
# =---  (_ _) _ __ ___   _ __    ___   _ __  _| |_    |  \/  |  ___    __| | ___   ---=#  use    mytoolbox.demo("To show all the Functions")
# =---   | | | '_ ` _ \ | '_ \  / _ \ | '__)(_   _)   | |\/| | / _ \  / _` |/ __)  ---=#
# =---   | | | | | | | || |_) )( (_) )| |     | |_    | |  | |( (_) )( (_| |\__ \  ---=#
# =---  (___)|_| |_| |_|| .__/  \___/ |_|      \__)   |_|  |_| \___/  \__,_|(___/  ---=#
# =---                  |_|                                                        ---=#
# =====================================================================================#
import os
import sys
import random
import msvcrt



# =================================================================#
# =----------------   Install using PIP if needed    -------------=# #pip install --upgrade pip
# =================================================================#
try:
    import art
except ImportError:
    print("=================================================================")
    print("============== PIP Installing ART ===============================")
    print("=================================================================")
    os.system('pip install art')
    from art import *

try:
    import pyperclip
except ImportError:
    print("=================================================================")
    print("============== PIP Installing Pyperclip =========================")
    print("=================================================================")
    os.system('pip install pyperclip')
    import pyperclip

try:
    import time
except ImportError:
    print("=================================================================")
    print("============== PIP Installing Time ==============================")
    print("=================================================================")
    os.system('pip install time')
    import time

try:
    import winsound
except ImportError:
    print("=================================================================")
    print("============== PIP Installing WinSound ==========================")
    print("=================================================================")
    os.system('pip install winsound')
    import winsound

try:
    import easygui
except ImportError:
    print("=================================================================")
    print("============== PIP Installing EasyGui ===========================")
    print("=================================================================")
    os.system('pip install easygui')
    import easygui

#  ┌────────────────────────────────────────────────────────────────────┐
#  │       __     __                     _  _      _                    │
#  │       \ \   / /  __ _  _ __   __ _ (_)| |__  | |  ___  ___         │
#  │        \ \ / /  / _` || '__| / _` || || '_ \ | | / _ \/ __|        │
#  │         \ V /  | (_| || |   | (_| || || |_) || ||  __/\__ \        │
#  │          \_/    \__,_||_|    \__,_||_||_.__/ |_| \___||___/        │
#  │                                                                    │
#  └────────────────────────────────────────────────────────────────────┘
color = "1F"
ColorList = ["0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C",
             "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A",
             "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E",
             "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B",
             "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F",
             "0A", "0B", "0C", "0E", "0F", "0A", "0B", "0C", "0E", "0F", ]
ColorList = iter(ColorList)


# For Colored Text
class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


#  ┌─────────────────────────────────────────────────────────────────────┐
#  │        _____                      _    _                            │
#  │       |  ___| _   _  _ __    ___ | |_ (_)  ___   _ __   ___         │
#  │       | |_   | | | || '_ \  / __|| __|| | / _ \ | '_ \ / __|        │
#  │       |  _|  | |_| || | | || (__ | |_ | || (_) || | | |\__ \        │
#  │       |_|     \__,_||_| |_| \___| \__||_| \___/ |_| |_||___/        │
#  │                                                                     │
#  └─────────────────────────────────────────────────────────────────────┘
# ==========================================#
# =----------------   DEMO    -------------=#
# ==========================================#
def demo():
    ''' Demo this Module'''
    pink("mytoolbox.Pink()")
    blue("mytoolbox.Blue()")
    green("mytoolbox.Green()")
    red("mytoolbox.Red()")
    yellow("mytoolbox.Yellow()")
    underline("mytoolbox.Underline()")
    print("-----------------------------")
    print("OpenLink(Link)")
    print("mytoolbox.OpenLink('www.google.com')")
    print("get=mytoolbox.Get()")
    print("mytoolbox.Screen(80,40)")
    print("mytoolbox.Paste()")
    print("mytoolbox.SetColor('0A')")
    print("mytoolbox.Quit()")
    print("mytoolbox.ToClipboard('Hello')")
    print("mytoolbox.Line(7)")
    return


#  ┌─────────────────────────────────────────────────────────────────────────────────────────┐
#  │        ____         _         _        __  ____                                         │
#  │       |  _ \  _ __ (_) _ __  | |_     / / / ___|   ___  _ __   ___   ___  _ __          │
#  │       | |_) || '__|| || '_ \ | __|   / /  \___ \  / __|| '__| / _ \ / _ \| '_ \         │
#  │       |  __/ | |   | || | | || |_   / /    ___) || (__ | |   |  __/|  __/| | | |        │
#  │       |_|    |_|   |_||_| |_| \__| /_/    |____/  \___||_|    \___| \___||_| |_|        │
#  │                                                                                         │
#  └─────────────────────────────────────────────────────────────────────────────────────────┘
# ==========================================#
# =----------------   Pink    -------------=#
# ==========================================#
def pink(txt:str) -> None:
    '''Print Pink Text'''
    print(bcolors.PINK + txt + bcolors.ENDC)
    return

# ============================================#
# =----------------   Blue    ---------------=#
# ============================================#
def blue(txt:str) -> None:
    '''Print Blue Text'''
    print(bcolors.BLUE + txt + bcolors.ENDC)
    return

# ============================================#
# =----------------   Green    --------------=#
# ============================================#
def green(txt:str) -> None:
    '''Print Green Text'''
    print(bcolors.GREEN + txt + bcolors.ENDC)
    return

# ============================================#
# =----------------   RED    ----------------=#
# ============================================#
def red(txt:str) -> None:
    '''Print Red Text'''
    print(bcolors.RED + txt + bcolors.ENDC)
    return

# ============================================#
# =----------------   Yellow    -------------=#
# ============================================#
def yellow(txt:str) -> None:
    '''Print Yellow Text'''
    print(bcolors.YELLOW + txt + bcolors.ENDC)
    return

# ===================================================#
# =----------------   Underline    -----------------=#
# ===================================================#
def underline(txt:str) -> None:
    '''Print Underlined Text'''
    print(bcolors.UNDERLINE + txt + bcolors.ENDC)
    return

# =====================================================#
# =-------------------   Line    ---------------------=#
# =====================================================#
def line(lines:int) -> None:
    '''Print a set of ------ Lines'''
    for x in range(0, lines):
        print("-----------------------------------------------------------------------")
        return


# ============================================#
# =--------------   CLS    ------------------=#
# ============================================#
def cls() -> None:
    '''Clear the Screen'''
    CMD('CLS')
    return

# ============================================#
# =------------   Clear    ------------------=#
# ============================================#
def clear() -> None:
    '''Clear the Screen'''
    CMD('CLS')
    return

# ===================================================#
# =---------------    Set Screen Size     ----------=#
# ===================================================#
def screen(x:int, y:int) -> None:
    '''Set the Screen Size'''
    CMD('mode con: cols=' + str(x) + ' lines=' + str(y))
    return

# ========================================================#
# =---------------   Set Screen Color    ----------------=#
# ========================================================#
def set_Color(color:str) -> None:
    '''Set the Screen Color'''
    CMD("Color " + color)
    return

# ========================================================#
# =----   Box it, Put Border around, Put in Box     -----=#
# ========================================================#
def put_A_Border_Around(txt:str) -> str:
    ''' Returns the text with a border around it '''
    lines = txt.splitlines()
    width = max(len(s) for s in lines)
    res = ['#  ┌' + '─' * width + '┐']
    for s in lines:
        res.append('#  │' + (s + ' ' * width)[:width] + '│')
    res.append('#  └' + '─' * width + '┘')
    return '\n'.join(res)

# ========================================================#
# =----            Comment Box for Code             -----=#
# ========================================================#
def comment_TextArt_Box_For_Code(txt:str)->str:
    ''' Large Text for Commenting in Code '''
    # print(put_A_Border_Around("This is text"))
    return put_A_Border_Around(get_TextArt(txt))


#  ┌───────────────────────────────────────────────────────────┐
#  │     _____              _              _           _       │
#  │    |_   _|  ___ __  __| |_           / \    _ __ | |_     │
#  │      | |   / _ \\ \/ /| __| _____   / _ \  | '__|| __|    │
#  │      | |  |  __/ >  < | |_ |_____| / ___ \ | |   | |_     │
#  │      |_|   \___|/_/\_\ \__|       /_/   \_\|_|    \__|    │
#  │                                                           │
#  └───────────────────────────────────────────────────────────┘
# ===================================================#
# =------  Print Every Version of TextArt    -------=#
# ===================================================#
def print_Every_Version_Of_Text(txt:str) -> None:
    '''Prints Every Version of Text Art'''
    List_of_Fonts = ['1943', '1row', '3-d', '3d_diagonal', '3x5', '4max', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alligator3', 'alpha', 'alphabet', 'amc3line', 'amc3liv1', 'amcaaa01', 'amcneko', 'amcrazo2', 'amcrazor', 'amcslash', 'amcthin', 'amctubes', 'amcun1', 'antrophobia', 'aquaplan', 'arrows', 'asc', 'ascii', 'ascii_new_roman', 'assalt_m', 'asslt_m', 'atc', 'atc_gran', 'atlantic', 'avatar', 'awcute', 'awesome', 'b1ff', 'banner', 'banner3', 'banner3-d', 'banner4', 'barbwire', 'basic', 'battlesh', 'baz_bil', 'bear', 'beer_pub', 'bell', 'benjamin', 'big', 'bigchief', 'bigfig', 'binary', 'black_bubble', 'black_square', 'block', 'block2', 'bold_fraktur', 'bold_script', 'bolger', 'braced', 'bright', 'broadway', 'bubble', 'bulbhead', 'c1', 'c2', 'c_ascii', 'c_consen', 'calgphy2', 'caligraphy', 'cards', 'carrier1', 'carrier2', 'catwalk', 'celtic', 'char1', 'char2', 'char3', 'char4', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'chartr', 'chartri', 'chinese_mafia', 'chiseled', 'chunky', 'cjk', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'cola', 'colossal', 'com_sen', 'computer', 'contessa', 'contouring1', 'contouring2', 'contouring3', 'contouring4', 'contrast', 'coptic1', 'coptic2', 'cranky', 'crawford', 'cricket', 'curly', 'currency', 'cute1', 'cute2', 'cute3', 'cyberlarge', 'cybermedium', 'cybersmall', 'cygnet', 'danc4', 'dancingfont', 'decimal', 'defleppard', 'diamond', 'dietcola', 'digital', 'dirty', 'dirty2', 'doh', 'doom', 'dotmatrix', 'dotted', 'double', 'doubleshorts', 'drako', 'drpepper', 'druid', 'dwarf', 'dwhistled', 'e_fist', 'ebbs_1', 'ebbs_2', 'eca', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'faces_of', 'fair_mea', 'fairligh', 'fancy1', 'fancy10', 'fancy100', 'fancy101', 'fancy102', 'fancy103', 'fancy104', 'fancy105', 'fancy106', 'fancy107', 'fancy108', 'fancy11', 'fancy12', 'fancy13', 'fancy14', 'fancy15', 'fancy16', 'fancy17', 'fancy18', 'fancy19', 'fancy2', 'fancy20', 'fancy21', 'fancy22', 'fancy23', 'fancy24', 'fancy25', 'fancy26', 'fancy27', 'fancy28', 'fancy29', 'fancy3', 'fancy30', 'fancy31', 'fancy32', 'fancy33', 'fancy34', 'fancy35', 'fancy36', 'fancy37', 'fancy38', 'fancy39', 'fancy4', 'fancy40', 'fancy41', 'fancy42', 'fancy43', 'fancy44', 'fancy45', 'fancy46', 'fancy47', 'fancy48', 'fancy49', 'fancy5', 'fancy50', 'fancy51', 'fancy52', 'fancy53', 'fancy54', 'fancy55', 'fancy56', 'fancy57', 'fancy58', 'fancy59', 'fancy6', 'fancy60', 'fancy61', 'fancy62', 'fancy63', 'fancy64', 'fancy65', 'fancy66', 'fancy67', 'fancy68', 'fancy69', 'fancy7', 'fancy70', 'fancy71', 'fancy72', 'fancy73', 'fancy74', 'fancy75', 'fancy76', 'fancy77', 'fancy78', 'fancy79', 'fancy8', 'fancy80', 'fancy81', 'fancy82', 'fancy83', 'fancy84', 'fancy85', 'fancy86', 'fancy87', 'fancy88', 'fancy89', 'fancy9', 'fancy90', 'fancy91', 'fancy92', 'fancy93', 'fancy94', 'fancy95', 'fancy96', 'fancy97', 'fancy98', 'fancy99', 'fantasy', 'fasion', 'fbr1', 'fbr12', 'fbr2', 'fbr_stri', 'fbr_tilt', 'filter', 'finalass', 'fire_font-s', 'fireing', 'flip', 'flipped', 'flyn_sh', 'foreign_friends', 'fourtops', 'fp1', 'fp2', 'fraktur', 'fraktur2', 'full_width', 'funface', 'funfaces', 'funky_dr', 'funky_fresh', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'georgi16', 'georgia11', 'ghost', 'ghost_bo', 'ghoulish', 'glenyn', 'goofy', 'gothic', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'greek_legends', 'green_be', 'h4k3r', 'hades', 'handwriting1', 'handwriting2', 'hazy', 'heartleft', 'heartright', 'heavy_me', 'henry3d', 'heroboti', 'high_noo', 'hills', 'hippie', 'hollywood', 'home_pak', 'horizontalleft', 'horizontalright', 'house_of', 'hypa_bal', 'hyper', 'hyves', 'icl-1900', 'impossible', 'inc_raw', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics', 'jacky', 'jazmine', 'katakana', 'keyboard', 'kgames_i', 'kik_star', 'knight', 'knight2', 'knob', 'krak_out', 'larry3d', 'lcd', 'lean', 'letters', 'lildevil', 'lilia', 'lineblocks', 'lockergnome', 'lopioo', 'love1', 'love2', 'madrid', 'malayalam', 'marquee', 'maxfour', 'merlin1', 'merlin2', 'messletters', 'mike', 'mini', 'minion', 'mirror', 'mirror_flip', 'modular', 'monospace', 'morse', 'moscow', 'muzzle', 'nancyj', 'nancyj-fancy', 'nancyj-underlined', 'native_lands', 'nfi1', 'nipples', 'nscript', 'nvscript', 'o8', 'octal', 'ogre', 'oldbanner', 'os2', 'paranormal', 'parenthesized', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'puzzle', 'pyramid', 'rammstein', 'rectangles', 'red_phoenix', 'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runyc', 'rusify', 'russian', 'santaclara', 'sarah', 'sblood', 'scammer', 'script', 'serifcap', 'shadow', 'shimrod', 'short', 'slammer', 'slant', 'slide', 'slscript', 'small', 'smallcaps', 'smallcaps2', 'smallcaps3', 'smisome1', 'smkeyboard', 'smooth1', 'smooth2', 'smpoison', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'soft', 'special', 'speed', 'spliff', 'stacey', 'stampate', 'stampatello', 'standard', 'starwars', 'stellar', 'stforek', 'stop', 'straight', 'strange', 'strikethrough', 'sub-zero', 'subscript', 'sunday_cuddle', 'superscript', 'swampland', 'swan', 'sweet', 'swirly', 'symbols', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'thin2', 'thin3', 'threepoint', 'ticks', 'ticksslant', 'tiles', 'tinker-toy', 'tiny', 'tiny2', 'tombstone', 'trek', 'tsalagi', 'tsn_base', 'tubular', 'twin_cob', 'twisted', 'twopoint', 'type_set', 'ucf_fan', 'ugalympi', 'unarmed', 'univers', 'upside_down', 'usa', 'usa_pq', 'usaflag', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'varsity', 'vortron', 'war_of_w', 'wavy', 'weird', 'wetletter', 'whimsy', 'white_bubble', 'white_square', 'wiggly', 'wow', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xtimes', 'xtty', 'xttyb', 'yie-ar', 'yie_ar_k', 'z-pilot', 'zig_zag', 'zone7']
    for temp_font in List_of_Fonts:
        print("\n"+temp_font)
        print(art.text2art(txt,temp_font))
    #print_Every_Version_Of_Text("AEIOU BCDFGHI")
    return

# ===================================================#
# =-------------  Print TextArt    -----------------=#
# ===================================================#
def print_text_Art(txt:str) -> None:
    '''Print Text Art'''
    print(art.text2art(txt))
    return

# ===================================================#
# =-------------  Get TextArt    -------------------=#
# ===================================================#
def get_TextArt(txt:str) -> str:
    ''' Get Text Art'''
    return art.text2art(txt)

# ===================================================#
# =----------  Get Specific TextArt    -------------=#
# ===================================================#
def get_TextArt_By_Font(txt:str, font:str) -> str:
    ''' Get Specific Text Art'''
    # Sample:   print(get_TextArt_By_Font("Hello", "3x5"))
    to_Clipboard(art.text2art(txt, font))
    return art.text2art(txt, font)


#  ┌─────────────────────────────────────────┐
#  │      ___                       _        │
#  │     |_ _| _ __   _ __   _   _ | |_      │
#  │      | | | '_ \ | '_ \ | | | || __|     │
#  │      | | | | | || |_) || |_| || |_      │
#  │     |___||_| |_|| .__/  \__,_| \__|     │
#  │                 |_|                     │
#  └─────────────────────────────────────────┘
# ============================================#
# =----------------   GET    ----------------=#
# ============================================#
def get() -> str:
    '''Input a Single Character, works in the Command Windows but not the PyCharm IDE, unless Configuration, Emulate Terminal in Output Console '''
    get = msvcrt.getwch()
    Ascii = ord(get)
    # print(Ascii)
    if Ascii == 8: get = "BACKSPACE"
    if Ascii == 13: get = "RETURN"
    if Ascii == 32: get = "SPACE"
    if Ascii == 9: get = "TAB"
    if Ascii == 27: get = "ESCAPE"
    get = str(get.upper())
    print(get)
    if (get == "Z"):
        get = "Z" + msvcrt.getwch()
        get = get.upper()
        print(get)
    return get

# ============================================#
# =--------------   Pause    ----------------=#
# ============================================#
def pause() -> None:
    '''Pause'''
    print(". . .")
    msvcrt.getwch()
    return

# ============================================#
# =--------   Press Any Key    --------------=#
# ============================================#
def press_Any_Key() -> None:
    '''Press any key'''
    print("Press Any Key...")
    msvcrt.getwch()
    return


# ============================================#
# =-----   Check Scroll Lock State    -------=#
# ============================================#
def get_ScrollLock_state():
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_SCROLL=0x91   # All the other ones are at  https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_SCROLL)





#  ┌────────────────────────────────────────────────────────────────┐
#  │       ____  _  _         _                              _      │
#  │      / ___|| |(_) _ __  | |__    ___    __ _  _ __   __| |     │
#  │     | |    | || || '_ \ | '_ \  / _ \  / _` || '__| / _` |     │
#  │     | |___ | || || |_) || |_) || (_) || (_| || |   | (_| |     │
#  │      \____||_||_|| .__/ |_.__/  \___/  \__,_||_|    \__,_|     │
#  │                  |_|                                           │
#  └────────────────────────────────────────────────────────────────┘
# ===================================================#
# =------------    Print Clipboard     -------------=#
# ===================================================#
def print_Clipboard() -> None:
    '''Print what is on the Clipboard'''
    print(str(pyperclip.paste()))
    return

# ===================================================#
# =------------      Get Clipboard     -------------=#
# ===================================================#
def get_Clipboard() -> str:
    ''' Return what is on the Clipboard '''
    return str(pyperclip.paste())

# =====================================================#
# =----------------   To Clipboard    -----------------=#
# =====================================================#
def to_Clipboard(txt:str) -> None:
    '''Put Text onto the Clipboard'''
    pyperclip.copy(txt)
    return

# =====================================================#
# =-------------   Clear Clipboard    -----------------=#
# =====================================================#
def to_Clipboard() -> None:
    ''' Clear the Clipboard '''
    pyperclip.copy("")
    return

# ============================================#
# =------  Wait until Clipboard Change  -----=#
# ============================================#
def wait_Until_Clipboard_Change()->None:
    original_Clipboard=str(pyperclip.paste())
    while original_Clipboard == str(pyperclip.paste()):
        time.sleep(.25)
    return



#  ┌─────────────────────────────────────┐
#  │      _____  ___  __  __  _____      │
#  │     |_   _||_ _||  \/  || ____|     │
#  │       | |   | | | |\/| ||  _|       │
#  │       | |   | | | |  | || |___      │
#  │       |_|  |___||_|  |_||_____|     │
#  │                                     │
#  └─────────────────────────────────────┘
# =====================================================#
# =-------------------   Sleep    --------------------=#
# =====================================================#
def sleep(seconds:int) -> None:
    '''Sleep for a set time in Miliseconds'''
    time.sleep(seconds)
    return

# =====================================================#
# =-------------------    Wait    --------------------=#
# =====================================================#
def wait(seconds:int) -> None:
    ''' Wait for a set time in Seconds'''
    time.sleep(seconds)
    return

# ============================================#
# =------      Time Stamp           ---------=#
# ============================================#
def timestamp()->str:
    ''' Return the TimeStamp year_month_day_'''
    import datetime
    now = datetime.datetime.now()
    timestamp=str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)
    return timestamp


#  ┌──────────────────────────────────────────────────┐
#  │        ____    ___   _   _  _   _  ____          │
#  │       / ___|  / _ \ | | | || \ | ||  _ \         │
#  │       \___ \ | | | || | | ||  \| || | | |        │
#  │        ___) || |_| || |_| || |\  || |_| |        │
#  │       |____/  \___/  \___/ |_| \_||____/         │
#  │                                                  │
#  └──────────────────────────────────────────────────┘
# ============================================#
# =------         Beep              ---------=#
# ============================================#
def beep() -> None:
    ''' Beep Sound '''
    frequency = 1500
    duration = 300  # 1000 is 1 second
    winsound.Beep(frequency, duration)
    return

# ============================================#
# =------         Blip              ---------=#
# ============================================#
def blip() -> None:
    ''' Very short Blip Sound '''
    frequency = 800
    duration = 50  # 1000 is 1 second
    winsound.Beep(frequency, duration)
    return



#  ┌───────────────────────────────────────────────────────────────────┐
#  │        ____    ___   ____             ____  __  __  ____          │
#  │       |  _ \  / _ \ / ___|           / ___||  \/  ||  _ \         │
#  │       | | | || | | |\___ \   _____  | |    | |\/| || | | |        │
#  │       | |_| || |_| | ___) | |_____| | |___ | |  | || |_| |        │
#  │       |____/  \___/ |____/           \____||_|  |_||____/         │
#  │                                                                   │
#  └───────────────────────────────────────────────────────────────────┘
# ============================================#
# =------      Does File Exist      ---------=#
# ============================================#
def does_File_Exist(filename:str) -> bool:
    ''' Returns Bool True or False if a file exists '''
    return os.path.exists(filename)

# ===================================================#
# =--------------   Windows Title    ---------------=#
# ===================================================#
def title(txt:str) -> None:
    '''Change the Window Title'''
    CMD("Title " + txt)
    return

# ============================================#
# =--------------   CMD    ------------------=#
# ============================================#
def cmd(txt:str) -> str:
    '''Enter a Command into the Shell, return results'''
    results = os.system(txt)
    return results

# ============================================#
# =------   Environment Variable    ---------=#
# ============================================#
def env_Var(txt:str) -> str:
    '''Get the value of an Environment Varaible'''
    return os.environ[txt]

# ============================================#
# =------   Append Text to File     ---------=#
# ============================================#
def append_Text_To_File(txt:str, filename:str) -> None:
    myfile = open(filename, 'a')
    print(txt, file=myfile)
    myfile.close()
    return

# ===============================================================================#
# =-----------------------     Notepad or Notepad++     ------------------------=#
# ===============================================================================#
def notepad(filename:str) -> None:
    '''Open a File in Notepad, and use NotePad++ if available'''
    results = CMD('Start Notepad.exe ' + filename)
    CLS()
    if (results == 1):
        CMD('Start Notepad++.exe ' + filename)
    CLS()
    return



#  ┌──────────────────────────────────┐
#  │         ____  _   _  ___         │
#  │        / ___|| | | ||_ _|        │
#  │       | |  _ | | | | | |         │
#  │       | |_| || |_| | | |         │
#  │        \____| \___/ |___|        │
#  │                                  │
#  └──────────────────────────────────┘
# ============================================#
# =------         Message Box       ---------=#
# ============================================#
def msg_Bosx(title:str, txt:str) -> None:
    ''' Windows Message Box '''
    easygui.msgbox(txt,title)
    return


#  ┌─────────────────────────────────────────┐
#  │        ___  _   _  _____   ___          │
#  │       |_ _|| \ | ||  ___| / _ \         │
#  │        | | |  \| || |_   | | | |        │
#  │        | | | |\  ||  _|  | |_| |        │
#  │       |___||_| \_||_|     \___/         │
#  │                                         │
#  └─────────────────────────────────────────┘
# ============================================#
# =------   Am I 32bit or 64bit     ---------=#
# ============================================#
def am_I_32Bit_or_64Bit() -> str:
    ''' Is this a 64bit or 32bit Interpreter?'''
    import struct;
    print(struct.calcsize("P") * 8)
    return str(struct.calcsize("P") * 8)

# ============================================#
# =------       Random Number       ---------=#
# ============================================#
def random_Number() -> float:
    ''' Returns a Random Number '''
    random.seed()
    return random.random()

# ============================================#
# =------   Current Directory       ---------=#
# ============================================#
def current_Directory()->str:
    return os.getcwd()

#  ┌────────────────────────────────────────┐
#  │        __  __  _                       │
#  │       |  \/  |(_) ___   ___            │
#  │       | |\/| || |/ __| / __|           │
#  │       | |  | || |\__ \| (__  _         │
#  │       |_|  |_||_||___/ \___|(_)        │
#  │                                        │
#  └────────────────────────────────────────┘
# =============================================#
# =-------------   Open Links    -------------=#
# =============================================#
def open_Link(Link:str) -> None:
    '''Open a link in the Browser'''
    ToClipboard(str(Link));  # Put Link on Clipboard
    CMD('Start \"URL\" \"' + str(Link) + '\" ')
    return

# ===================================================#
# =------------------   Exit/Quit   ----------------=#
# ===================================================#
def quit() -> None:
    '''Exit the Program'''
    Goodbye = "                    |\r\n                \\       /\r\n                  .---. \r\n             \'-.  |   |  .-\'\r\n               ___|   |___\r\n          -=  [           ]  =-\r\n              `---.   .---\' \r\n           __||__ |   | __||__\r\n           \'-..-\' |   | \'-..-\'\r\n             ||   |   |   ||\r\n             ||_.-|   |-,_||\r\n           .-\"`   `\"`\'`   `\"-.\r\n   ___   .\'           _ _     \'.\r\n  / _ \\___   ___   __| | |__  _   _  ___ \r\n / /_\\/ _ \\ / _ \\ / _` | \'_ \\| | | |/ _ \\\r\n/ /_\\\\ (_) | (_) | (_| | |_) | |_| |  __/\r\n\\____/\\___/ \\___/ \\__,_|_.__/ \\__, |\\___|\r\n                              |___/\r\n"
    SetColor("2F")
    CLS()
    print(Goodbye)
    Sleep(.5)
    sys.exit()
    return

