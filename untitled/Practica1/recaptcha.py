def recaptcha_check(check):
    try:
        for frame in browser.find_element("TAG_NAME","iframe")
            browser.switch_to.default_content()
            browser.switch_to.frame(frame)
            for x in ['@class=', '@id=','@name=','@for=','text()=']:
                try:
                    browser.find_element("xpath",f"//*[{x}'{check}']")
                    return True
                except: continue
    except: return False


def frame_select():
