def daytoJulian(year,month,day):
    import datetime
    i,j,k = 0,0,0

    julianDay=[]
    while i <= len(year)-1:
        while j <= len(month)-1:
            while k <= len(day)-1:
                julian = str(datetime.datetime.strptime('{0}-{1}-{2}'.format(year[i],month[j], day[k]),
                '%Y-%m-%d').timetuple().tm_yday).zfill(3)
                julianDay.append(julian)

                k += 1
            j+= 1
        i+=1


    return julianDay



year = ["2018"]
month = ["03"]
day = ["19","20"]

julianDay = daytoJulian(year,month,day)

print(julianDay)
