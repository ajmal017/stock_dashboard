from connect import connect
import datetime as dt
import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np
import pandas as pd
import talib

matplotlib.use('TkAgg')

# Variables and Defaults
LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

style.use('ggplot')

fig = plt.figure()

currentDate = dt.datetime.today()
startDate = currentDate.strftime("%Y-%m-%d")
DataCounter = 9000
programName = 'btce'
resampleSize = "15Min"
timeFrame = 'ohlc'
candleWidth = 0.0001
paneCount = 1
topIndicator= 'none'
bottomIndicator= 'none'
middleIndicator= 'none'
chartLoad = True
darkColor ='#183A54'
lightColor='#00A3E0'
ticker = 'AAPl'
screen_width = 1280
screen_height = 720

EMAs = []
SMAs = []


# Functions

def loadChart(run):
    global chartLoad
    if run == 'start':
        chartLoad = True
    elif run == 'stop':
        chartLoad = False


# def tutorial():
#     # def leavemini(what):
#     #     what.destroy()
#     def page2():
#         tut.destroy()
#         tut2 = tk.Tk()
#
#         def page3():
#             tut2.destroy()
#             tut3 = tk.Tk()
#             tut3.wm_title('Part 3!')
#             label = ttk.Label(tut3, text='Part 3', font=NORM_FONT)
#             label.pack(side='top', fill='x', pady=10)
#             B1 = tk.Button(tut3, text='Done!', command=tut3.destroy)
#             B1.pack()
#             tut3.mainloop()
#
#         tut2.wm_title('Part 2!')
#         label = ttk.Label(tut2, text='Part 2', font=NORM_FONT)
#         label.pack(side='top', fill='x', pady=10)
#         B1 = tk.Button(tut2, text='Next', command=page3)
#         B1.pack()
#         tut2.mainloop()
#
#     tut = tk.Tk()
#     tut.wm_title('Tutorial')
#     label = ttk.Label(tut, text='What do you need help with?', font=NORM_FONT)
#     label.pack(side='top', fill='x', pady=10)
#
#     B1 = ttk.Button(tut, text='Overview of the application', command=page2)
#     B1.pack()
#
#     B2 = ttk.Button(tut, text='How do I trade with this client?', command=popupmsg('Not yet completed'))
#     B2.pack()
#
#     B3 = ttk.Button(tut, text='Indicator Questions/Help', command=popupmsg('Not yet completed'))
#     B3.pack()
#
#     tut.mainloop()


def addTopIndicator(what):
    global topIndicator, DataCounter

    if what == 'none':
        topIndicator = what
        DataCounter = 9000

    elif what =='rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text="Choose how many periods.")
        label.pack(side='top', fill='x', pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator, DataCounter
            topIndicator = []
            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(int(periods))

            topIndicator.append(group)
            DataCounter = 9000
            print('Set top indicator', group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == 'macd':
        topIndicator = 'macd'


def addMiddleIndicator(what):
    global middleIndicator, DataCounter

    if what != 'none':
        if middleIndicator == 'none':
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods')
                label = ttk.Label(midIQ, text='Choose number of periods.')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator, DataCounter
                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DataCounter = 9000
                    print('Middle indicator set to: ', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods')
                label = ttk.Label(midIQ, text='Choose number of periods.')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator, DataCounter
                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DataCounter = 9000
                    print('Middle indicator set to: ', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods')
                label = ttk.Label(midIQ, text='Choose number of periods.')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator, DataCounter
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DataCounter = 9000
                    print('Middle indicator set to: ', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods')
                label = ttk.Label(midIQ, text='Choose number of periods.')
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator, DataCounter
                    # middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DataCounter = 9000
                    print('Middle indicator set to: ', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

    else:
        middleIndicator = 'none'

def addBottomIndicator(what):
    global bottomIndicator, DataCounter

    if what == 'none':
        bottomIndicator = what
        DataCounter = 9000

    elif what == 'apo':
        bottomIndicator = 'apo'

def changeTimeFrame(tf):
    global timeFrame, DataCounter, startDate
    if tf == 7 and resampleSize == '1Min':
        popupmsg('Too much data chosen.  Choose a smaller time frame or a higher OHLC interval.')

    else:
        startDate = (currentDate - dt.timedelta(days=tf)).strftime("%Y-%m-%d")
        timeFrame = tf
        DataCounter = 9000


def changeSampleSize(size, width):
    global resampleSize, DataCounter, candleWidth
    if timeFrame == '7D' and resampleSize == '1Min':
        popupmsg('Too much data chosen.  Choose a smaller time frame or higher OHLC interval.')


    else:
        resampleSize = size
        DataCounter = 9000
        candleWidth = width


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('Warning')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    popup.mainloop()


def changeExchange(toWhat, pn):
    global exchange, DataCounter, programName
    exchange = toWhat
    programName = pn
    DataCounter = 9000


def animate(i):
    global DataCounter, resreshRate, ticker

    if chartLoad:
        if DataCounter > 12:
            try:
                ticker = ticker.upper()
                df = pd.DataFrame(connect(ticker, startDate))

                df.sort_values(['datetime'], ascending=False)
                df['datetime'] = pd.to_datetime(df['datetime'], utc=False).dt.tz_convert('US/Central')
                df.rename(columns={'date': 'Date', 'datetime': 'Datetime', 'hi': 'High', 'last': 'Close',
                                   'lo': 'Low', 'opn': 'Open', 'vl': 'Volume'}, inplace=True)
                df['Date'] = mdates.datestr2num(df['Date'])
                df['Datetime'] = mdates.date2num(df['Datetime'])
                df['High'] = df['High'].astype(float)
                df['Low'] = df['Low'].astype(float)
                df['Open'] = df['Open'].astype(float)
                df['Close'] = df['Close'].astype(float)
                df['Volume'] = df['Volume'].astype(float)

                if topIndicator != 'none' and bottomIndicator != 'none':
                    # Main Graph
                    ax = plt.subplot2grid((6, 4), (1, 0), rowspan=3, colspan=4)

                    # Volume
                    a2 = plt.subplot2grid((6, 4), (4, 0), sharex=ax, rowspan=1, colspan=4)

                    # Bottom Indicator
                    a3 = plt.subplot2grid((6, 4), (5, 0), sharex=ax, rowspan=1, colspan=4)

                    # Top Indicator
                    a0 = plt.subplot2grid((6, 4), (0, 0), sharex=ax, rowspan=1, colspan=4)

                elif topIndicator != 'none':
                    # Main Graph
                    ax = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4)

                    # Volume
                    a2 = plt.subplot2grid((6, 4), (5, 0), sharex=ax, rowspan=1, colspan=4)

                    # Top Indicator
                    a0 = plt.subplot2grid((6, 4), (0, 0), sharex=ax, rowspan=1, colspan=4)

                elif bottomIndicator != 'none':
                    # Main Graph
                    ax = plt.subplot2grid((6, 4), (0, 0), rowspan=4, colspan=4)

                    # Volume
                    a2 = plt.subplot2grid((6, 4), (4, 0), sharex=ax, rowspan=1, colspan=4)

                    # Bottom Indicator
                    a3 = plt.subplot2grid((6, 4), (5, 0), sharex=ax, rowspan=1, colspan=4)

                else:
                    # Main Graph
                    ax = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)

                    # Volume
                    a2 = plt.subplot2grid((6, 4), (5, 0), sharex=ax, rowspan=1, colspan=4)


                candlestick_ohlc(ax, df[['Datetime', 'Open', 'High', 'Low', 'Close']].values, colorup='g', colordown='r', width=candleWidth)

                a2.fill_between(df['Datetime'], 0, df['Volume'].values, facecolor=darkColor)

                if middleIndicator != 'none':
                    for eachMA in middleIndicator:
                        if eachMA[0] == 'sma':
                            sma = talib.SMA(df['Close'], timeperiod=eachMA[1])
                            label = 'SMA-' + str(eachMA[1])
                            ax.plot(df['Datetime'], sma, label=label)
                            ax.legend()

                        if eachMA[0] == 'ema':
                            ema = talib.EMA(df['Close'], timeperiod=eachMA[1])
                            label = 'EMA-' + str(eachMA[1])
                            ax.plot(df['Datetime'], ema, label=label)
                            ax.legend()

                if topIndicator != 'none':
                    for eachTopInd in topIndicator:
                        if eachTopInd[0] == 'rsi':
                            rsi = talib.RSI(np.asarray(df['Close']), timeperiod=eachTopInd[1])
                            a0.plot(df['Datetime'], rsi)
                            a0.fill_between(df['Datetime'], rsi, 70, where=(rsi >= 70), facecolor='r', edgecolor='r',
                                            alpha=.5)
                            a0.fill_between(df['Datetime'], rsi, 30, where=(rsi <= 30), facecolor='g', edgecolor='g',
                                            alpha=.5)
                            a0.axhline(70, color='k')
                            a0.axhline(30, color='k')

                            a0.set_ylabel('RSI')
                            plt.setp(a0.get_xticklabels(), visible=False)
                            plt.setp(ax.get_xticklabels(), visible=False)
                            a0.set_title('{} Prices\nLast Price: $'.format(ticker) + str(round(df['Close'][len(df) - 1], 2)))

                            for label in a2.xaxis.get_ticklabels():
                                label.set_rotation(45)

                    if topIndicator == 'macd':
                        macd = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
                        a0.plot(df['Datetime'], macd[0], label='MACD', color='b')
                        a0.plot(df['Datetime'], macd[1], label='Signal', color='g')
                        a0.plot(df['Datetime'], macd[2], label='Hist', color='r')
                        a0.axhline(0, color='k')

                        a0.set_ylabel('MACD')
                        plt.setp(a0.get_xticklabels(), visible=False)
                        plt.setp(ax.get_xticklabels(), visible=False)
                        a0.set_title('{} Prices\nLast Price: $'.format(ticker) + str(round(df['Close'][len(df) - 1], 2)))
                        a0.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=3, borderaxespad=0)

                        for label in a2.xaxis.get_ticklabels():
                            label.set_rotation(45)

                else:
                    ax.set_title('{} Prices\nLast Price: $'.format(ticker) + str(round(df['Close'][len(df) - 1], 2)))

                if bottomIndicator != 'none':
                    if bottomIndicator == 'apo':
                        apo = talib.APO(np.asarray(df['Close']), fastperiod=14, slowperiod=30, matype=0)
                        a3.plot(df['Datetime'], apo, color='k', linewidth=1)
                        a3.axhline(0, color='k')
                        a3.fill_between(df['Datetime'], apo, 0, where=(apo > 0), facecolor='g', edgecolor='g', alpha=.5)
                        a3.fill_between(df['Datetime'], apo, 0, where=(apo <= 0), facecolor='r', edgecolor='r', alpha=.5)

                        a3.set_ylabel('APO')

                        for label in a3.xaxis.get_ticklabels():
                            label.set_rotation(45)

                        plt.setp(ax.get_xticklabels(), visible=False)
                        plt.setp(a2.get_xticklabels(), visible=False)


                # ax.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)

                ax.xaxis.set_major_locator(mticker.MaxNLocator(15))
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                ax.set_ylabel('Price')
                a2.set_ylabel('Volume')
                ax.grid(True)
                plt.setp(ax.get_xticklabels(), visible=False)
                plt.xticks(rotation=45)

            except Exception as e:
                print('Failed because of ', str(e))

        else:
            DataCounter += 1

# Classes

class StockDashboard(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'Stock Analysis Dashboard')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Save Settings', command=lambda: popupmsg('Not supported just yet!'))
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=quit)
        menu_bar.add_cascade(label='File', menu=file_menu)

        dataTF = tk.Menu(file_menu, tearoff=1)
        dataTF.add_command(label='Today', command=lambda: changeTimeFrame(0))
        dataTF.add_command(label='1 Day', command=lambda: changeTimeFrame(1))
        dataTF.add_command(label='3 Day', command=lambda: changeTimeFrame(3))
        dataTF.add_command(label='1 Week', command=lambda: changeTimeFrame(7))
        menu_bar.add_cascade(label='Data Time Frame', menu=dataTF)

        OHLCI = tk.Menu(menu_bar, tearoff=1)
        OHLCI.add_command(label='1 Minute', command=lambda: changeSampleSize('1Min', 0.0005))
        OHLCI.add_command(label='5 Minute', command=lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label='15 Minute', command=lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label='30 Minute', command=lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label='1 Hour', command=lambda: changeSampleSize('1Hr', 0.032))
        OHLCI.add_command(label='3 Hour', command=lambda: changeSampleSize('3Hr', 0.096))
        menu_bar.add_cascade(label='OHLC Interval', menu=OHLCI)

        topIndi = tk.Menu(menu_bar, tearoff=1)
        topIndi.add_command(label='None', command=lambda: addTopIndicator('none'))
        topIndi.add_command(label='RSI', command=lambda: addTopIndicator('rsi'))
        topIndi.add_command(label='MACD', command=lambda: addTopIndicator('macd'))
        menu_bar.add_cascade(label='Top Indicator', menu=topIndi)

        mainI = tk.Menu(menu_bar, tearoff=1)
        mainI.add_command(label='None', command=lambda: addMiddleIndicator('none'))
        mainI.add_command(label='SMA', command=lambda: addMiddleIndicator('sma'))
        mainI.add_command(label='EMA', command=lambda: addMiddleIndicator('ema'))
        menu_bar.add_cascade(label='Middle Indicator', menu=mainI)

        bottomI = tk.Menu(menu_bar, tearoff=1)
        bottomI.add_command(label='None', command=lambda: addBottomIndicator('none'))
        bottomI.add_command(label='Absolute Price Oscillator (APO)', command=lambda: addBottomIndicator('apo'))
        menu_bar.add_cascade(label='Bottom Indicator', menu=bottomI)


        tradeButton = tk.Menu(menu_bar, tearoff=1)
        tradeButton.add_command(label='Manual Trading', command=lambda: popupmsg('This is not live yet'))
        tradeButton.add_command(label='Automatic Trading', command=lambda: popupmsg('This is not live yet'))

        tradeButton.add_separator()

        tradeButton.add_command(label='Quick Buy', command=lambda: popupmsg('This is not live yet'))
        tradeButton.add_command(label='Quick Sell', command=lambda: popupmsg('This is not live yet'))

        tradeButton.add_separator()
        tradeButton.add_command(label='Set-up Quick Buy/Sell', command=lambda: popupmsg('This is not live yet'))

        menu_bar.add_cascade(label='Trading', menu= tradeButton)

        startStop = tk.Menu(menu_bar, tearoff= 1)
        startStop.add_command(label='Resume', command=lambda: loadChart('start'))
        startStop.add_command(label='Pause', command=lambda: loadChart('stop'))

        menu_bar.add_cascade(label='Resume/Pause Client', menu=startStop)


        # helpmenu = tk.Menu(menu_bar, tearoff=0)
        # helpmenu.add_command(label='Tutorial', command=tutorial)
        #
        # menu_bar.add_cascade(label='Help', menu=helpmenu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (StartPage, PageOne, TickerPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Trading Application', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Agree',
                             command=lambda: controller.show_frame(TickerPage))
        button1.pack()

        button2 = ttk.Button(self, text='Disagree',
                            command=quit)
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='Visit Page Two',
                             command=lambda: controller.show_frame(TickerPage))
        button2.pack()


class TickerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Stock Analysis Graphs', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text='Back to Home',
        #                     command=lambda: controller.show_frame(StartPage))
        #
        # button1.pack(side=tk.TOP)


        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=tk.TOP, anchor=tk.NW, fill=tk.BOTH, expand=True)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        ticker_label = tk.Label(self, text='Enter Ticker:')
        ticker_label.pack(side=tk.LEFT)
        ticker_entry = tk.Entry(self, width=10)
        ticker_entry.pack(side=tk.LEFT)

        def callback():
            global ticker
            ticker = ticker_entry.get()

        button_ticker = ttk.Button(self, text='Submit', command=callback)
        button_ticker.pack(side=tk.LEFT)

# Program Calls


app = StockDashboard()
app.geometry("{}x{}".format(screen_width, screen_height))
ani = animation.FuncAnimation(fig, animate, interval=5000)
app.mainloop()