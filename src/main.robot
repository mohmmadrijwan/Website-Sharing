*** Settings ***
Library           ../lib/lib.py

*** Variables ***	

*** Test Cases ***
Ticket_Creation
    [Tags]    Ticket
    [Setup]   
    Set Test Documentation    Creates Ticket based on criticality of the alerts
    WHILE    True    limit=NONE
        ${check}    ${data1}    ${data2}    detect_new_articles

        IF  ${check}
            ${paragraph}    fetch_article_content
            Log             ${paragraph}

            ${caption}      generate_caption    ${paragraph}
            Log             ${caption}

            getImage

            ${shortUrl}     shorten_url
            Log             ${shortUrl}

            saveToJsonFile

            openhtmlFile
        END
    END
    Set Test Message    Creates Ticket based on criticality of the alerts is done successfully
    

*** Keywords ***

