import urllib.parse as up

term_in = '201812'
cur_year = term_in[:4]


domain = "myportal.fhda.edu"
https = "https"

URL_LOGIN = "https://myportal.fhda.edu/cp/home/displaylogin"
URL_POST_LOGIN = "https://myportal.fhda.edu/cp/home/login"

ACTION_POST_SCHEDULE = "/PROD/bwskcrse.P_CrseSchdDetl"
ACTION_POST_CLASSDATE = "/PROD/bwckgens.p_proc_term_date"
ACTION_POST_GETSUBJECT = "/PROD/bwskfcls.P_GetCrse"
ACTION_POST_GETCOURSE = '/PROD/bwskfcls.P_GetCrse'

URL_LOGINOK = "https://myportal.fhda.edu/cps/welcome/loginok.html"
URL_LOGINNEXT = "https://myportal.fhda.edu/cp/home/next"

MARK_SERVERTIME = "var clientServerDelta = (new Date()).getTime() - "
MARK_SCHEDULETABLE = "Display course details for a student.,BORDER = 1,"

URL_NOCOURSEPAGE = "https://myportal.fhda.edu/site/coursestudio/default.html"
URL_LOGOUT = "https://myportal.fhda.edu/up/Logout?uP_tparam=frm&frm="

URL_SELECTSUBJECT = "/cp/ip/login?sys=sctssb&url=https://banssb.fhda.edu/PROD/bwskfcls.p_sel_crse_search"

MASK_COURSEINFO = (1, 2, 3, 4, 6, 7, 8, 9, 16, 17, 19)

FORM_GETSUBJECT = [
    ("rsts", "dummy"),
    ("crn", "dummy"),
    ("term_in", term_in),
    ("sel_day", "dummy"),
    ("sel_schd", "dummy"),
    ("sel_insm", "dummy"),
    ("sel_camp", "dummy"),
    ("sel_levl", "dummy"),
    ("sel_sess", "dummy"),
    ("sel_instr", "dummy"),
    ("sel_ptrm", "dummy"),
    ("sel_attr", "dummy"),
    ("sel_subj", "dummy"),
    ("sel_crse", ""),
    ("sel_title", ""),
    ("sel_from_cred", ""),
    ("sel_to_cred", ""),
    ("sel_ptrm", "%"),
    ("begin_hh", "0"),
    ("begin_mi", "0"),
    ("end_hh", "0"),
    ("end_mi", "0"),
    ("begin_ap", "x"),
    ("end_ap", "y"),
    ("path", "1"),
    ("SUB_BTN", "Course Search")
]

FORM_GETCOURSE = [
    ('term_in', term_in),
    ('sel_subj', 'dummy'),
    ('SEL_TITLE', ''),
    ('BEGIN_HH', '0'),
    ('BEGIN_MI', '0'),
    ('BEGIN_AP', 'a'),
    ('SEL_DAY', 'dummy'),
    ('SEL_PTRM', 'dummy'),
    ('END_HH', '0'),
    ('END_MI', '0'),
    ('END_AP', 'a'),
    ('SEL_CAMP', 'dummy'),
    ('SEL_SCHD', 'dummy'),
    ('SEL_SESS', 'dummy'),
    ('SEL_INSTR', 'dummy'),
    ('SEL_INSTR', '%'),
    ('SEL_ATTR', 'dummy'),
    ('SEL_ATTR', '%'),
    ('SEL_LEVL', 'dummy'),
    ('SEL_LEVL', '%'),
    ('SEL_INSM', 'dummy'),
    ('sel_dunt_code', ''),
    ('sel_dunt_unit', ''),
    ('call_value_in', ''),
    ('rsts', 'dummy'),
    ('crn', 'dummy'),
    ('path', '1'),
    ('SUB_BTN', 'View Sections')
]

TITLE_COURSE = (
    "CRN",
    "Subject",
    "Course"
    "Section",
    "Credit",
    "Title",
    "Days",
    "Time",
    "Capacity",
    "Actual",
    "Remaining",
    "Waitlist Capacity",
    "Waitlist Actual",
    "Waitlist Reamining",
    "Instructor",
    "Date",
    "Location",
    "Online Content"
)


def getLegalUrl(url):
    """
    domain must not contains the tailing /
    """
    p = up.urlparse(url)
    p = list(p)
    if p[1] == "":
        p[1] = domain
        p[0] = https

    res = up.urlunparse(p)
    return res

def getCourseTD(ele):
    if ele.name == 'td':
        if ele.parent.name == 'table' and ele.parent['class'][0] == 'datadisplaytable':
            return True
    return False


def outputHTML(text, filename):
    f = open(filename, "w+")
    f.write(text)
    f.close()
