from . import myportalapi as mp
from bs4 import BeautifulSoup
from . import mputil as util

MyPortal = mp.MP_Viewer("20295084", "bbf1120ag3")
MyPortal.Login()


def GetScheduleData(term):
    """
    This function passed the test.
    """
    MyPortal.Click("Registration")
    MyPortal.Click("View Your Class Schedule")
    MyPortal.PostForm(action=util.ACTION_POST_SCHEDULE, data={"term_in": term})

    raw = MyPortal.rawText
    soup = BeautifulSoup(raw, "html.parser")
    data = []
    table = soup.find('table', attrs={'summary': util.MARK_SCHEDULETABLE})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        tmp = [ele for ele in cols if ele]
        if len(tmp) > 0:
            data.append(tmp)
    return data


def GetClassList():
    MyPortal.Click("Students")
    MyPortal.Click("Go to My Courses and Instructor Email")
    soup = BeautifulSoup(MyPortal.rawText, "html.parser")
    table = soup.find('table', attrs={'id': 'sCourseList'})
    hrefs = table.find_all('a')
    classList = []
    for i in range(0, len(hrefs), 2):
        if hrefs[i].attrs['href'] != util.URL_NOCOURSEPAGE:
            classList.append((hrefs[i].string, hrefs[i + 1].string))
    return classList


def GetMessages():
    soup = BeautifulSoup(MyPortal.rawText, "html.parser")
    table = soup.find('table', attrs={'id': 'teaser_abm_tbl'})
    data = table.find_all('a')
    res = []
    for i in data:
        res.append((i.attrs['href'], i.string))
    return res


def GetClasses():
    MyPortal.Click("Registration")
    MyPortal.Click("Searchable Schedule of Classes")
    MyPortal.PostForm(util.ACTION_POST_CLASSDATE, data={
        "p_term": util.term_in, "p_calling_proc": "P_CrseSearch"})
    soup = BeautifulSoup(MyPortal.rawText, "html.parser")
    courses = soup.find_all('option')
    res = []
    for i in courses:
        if i.string == "All":
            break
        res.append((i.attrs['value'], i.string))
    return res


def GetSubject(subject):
    formData = util.FORM_GETSUBJECT[:]
    formData.append(("sel_subj", subject))
    MyPortal.PostForm(util.ACTION_POST_GETSUBJECT, data=formData)

    page = MyPortal.rawText
    page = page.replace('</tr>', '').replace('<tr>', '')
    page = page.replace('</TR>', '').replace('<TR>', '')
    soup = BeautifulSoup(page, "html.parser")
    courses = soup.find_all(util.getCourseTD)

    res = []
    for i in range(0, len(courses), 3):
        form = courses[i + 2].find('form')
        courseId = form.find('input', attrs={'name': 'SEL_CRSE'})
        res.append((
            courses[i].string,
            courses[i + 1].string,
            courseId.attrs['value']
        ))
    return res


def GetCourse(subject, course):
    formData = util.FORM_GETCOURSE[:]
    formData.append(('SEL_CRSE', course))
    formData.append(('sel_subj', subject))

    MyPortal.PostForm(util.ACTION_POST_GETCOURSE, data=formData)

    page = MyPortal.rawText
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', attrs={'class': 'datadisplaytable'})
    courses = table.find_all('tr')
    res = []
    for i in range(2, len(courses)):
        td = courses[i].find_all('td')
        tmp = []

        for j in util.MASK_COURSEINFO:
            ts = td[j].string
            if j == 16:
                ts = str(td[j].contents[0])+'P)'
            elif ts is not None:
                ts = ts.strip()
            tmp.append(ts)
        res.append(tmp)
    return res
