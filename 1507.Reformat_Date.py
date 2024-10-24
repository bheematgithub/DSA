class Solution:
    def reformatDate(self, date: str) -> str:
        mnt={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        dd=""
        if date[1].isdigit():
            dd=date[:2]
        else:
            dd="0"+date[0]
        res=f"{date[-4:]}-{mnt[date[-8:-5]]}-{dd}"
        return res
