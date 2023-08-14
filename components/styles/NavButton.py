custom_btn = """
QPushButton {
    width: 130px;
    height: 40px;
    color: #fff;
    border-radius: 5px;
    padding: 10px 25px;
    font-family: 'Lato', sans-serif;
    font-weight: 500;
    background: transparent;
    transition: all 0.3s ease;
    position: relative;
    box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5),
                7px 7px 20px 0px rgba(0,0,0,.1),
                4px 4px 5px 0px rgba(0,0,0,.1);
    outline: none;
}

QPushButton.btn-16 {
    border: none;
    color: #000;
}

QPushButton.btn-16:after {
    position: absolute;
    content: "";
    width: 0;
    height: 100%;
    top: 0;
    left: 0;
    direction: rtl;
    z-index: -1;
    box-shadow: -7px -7px 20px 0px #fff999,
                 -4px -4px 5px 0px #fff999,
                 7px 7px 20px 0px #000222,
                 4px 4px 5px 0px #000111;
    transition: all 0.3s ease;
}

QPushButton.btn-16:hover {
    color: #000;
}

QPushButton.btn-16:hover:after {
    left: auto;
    right: 0;
    width: 100%;
}

QPushButton.btn-16:active {
    top: 2px;
}
"""