| Section        | Element               | Locator Type | Locator                                              | Stability | Reason                          |
|----------------|----------------------|--------------|------------------------------------------------------|----------|---------------------------------|
| Login Page     | Username             | CSS          | input[id="userName"]                                 | Stable   | Uses unique id                  |
| Login Page     | Username             | XPath        | //input[@id="userName"]                              | Stable   | ID-based locator                |
| Login Page     | Password             | CSS          | input[placeholder="Password"]                        | Stable   | Meaningful attribute            |
| Login Page     | Password             | XPath        | //input[@placeholder="Password"]                     | Stable   | Readable attribute              |
| Practice Form  | First Name           | CSS          | input[placeholder="First Name"]                      | Stable   | Clear placeholder               |
| Practice Form  | Last Name            | CSS          | input[placeholder="Last Name"]                       | Stable   | Consistent UI attribute         |
| Practice Form  | Mobile Number        | CSS          | input[placeholder="Mobile Number"]                   | Stable   | Specific placeholder            |
| Books          | Select Items         | CSS          | a[href="/books?search=9781449325862"]                | Stable   | Direct link targeting           |
| Books          | Select Items         | XPath        | //a[@href="/books?search=9781449325862"]             | Stable   | Attribute-based                 |
| Practice Form  | Gender Radio Button  | CSS          | input[name="gender"][value="Male"]                   | Stable   | Multiple attributes             |
| Login Page     | Login Button         | CSS          | button[class="btn btn-primary"]:nth-of-type(1)       | Weak     | Uses index, not unique          |
| Books          | Add to Collection    | CSS          | div:nth-of-type(2) button[id="addNewRecordButton"]   | Weak     | Depends on DOM structure        |