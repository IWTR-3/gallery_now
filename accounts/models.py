# accoutns/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from posts.models import Review, Gallery, Artist, Exhibition


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        nickname = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    # required fileds
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='images/profile/')
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    # MTM fields

    followings = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False)
    like_exhibitions = models.ManyToManyField(
        Exhibition, related_name='like_users')
    like_reviews = models.ManyToManyField(Review, related_name="like_users")

    # status field

    is_artist = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


"""
strings = """
"""강경구	*	Kang kyung koo	*	회화
강관욱	*	Kang kwan wook	*	조각
강광	*	Kang kwang	*	회화
강남미	*	Kang nam mi	*	미술작가
강미영	*	kang mi young	*	시각기타
강봉규	*	Kang bong kyu	*	미술작가
강석영	*	Kang suk young	*	미술작가
강성원	*	Kang seong won	*	미술작가
강애란	*	Kang ai ran	*	미술작가
강연균	*	Kang yeon gyun	*	미술작가
강용면	*	Kang yong myeon	*	시각기타
강운	*	Kang un	*	시각기타
강익중	*	Kang ik joong	*	미술작가
강정완	*	Kang jeong wan	*	미술작가
강진모	*	Kang jin mo	*	미술작가
강진식	*	Kang jin sik	*	미술작가
강찬균	*	Kang chan gyun	*	미술작가
강찬모	*	Kang chan mo	*	미술작가
강태성	*	Kang tae seong	*	미술작가
강희덕	*	Kang hee duk	*	미술작가
계낙영	*	Kyea nak young	*	미술작가
고명근	*	Koh myung keun	*	시각기타
고영훈	*	Ko young hoon	*	시각기타
고정수	*	Koh jeong soo	*	시각기타
공성훈	*	Kong sung hun	*	미술작가
곽계정	*	Goak gae jeong	*	미술작가
곽남신	*	Kwak nam sin	*	미술작가
곽덕준	*	Kwak duck jun	*	미술작가
곽정명	*	Gwak jeong myeong	*	미술작가
곽훈	*	Kwak hoon	*	미술작가
구본주	*	Gu bon ju	*	시각기타
구본창	*	Koo bohn chang	*	미술작가
구자승	*	Koo cha soong	*	미술작가
권순철	*	Kwun sun cheol	*	미술작가
권순형	*	Kwon soon hyung	*	시각기타
권여현	*	Kwon yeo hyun	*	시각기타
권영우	*	Kwon young woo	*	회화
권옥연	*	 權玉淵	*	회화
권정호	*	Kwon jung ho	*	회화
금중기	*	Keum joong ki	*	미술작가
김경승	*	Kim kyung seung	*	미술작가
김경인	*	Kim kyung in	*	미술작가
김광문	*	Kim kwang moon	*	시각기타
김광우	*	Kim kwang woo	*	미술작가
김구림	*	Kim ku lim	*	미술작가
김근중	*	Kim keun joong	*	시각기타
김기라	*	Kim ki ra	*	공예
김기린	*	Kim gui line	*	미술작가
김기창	*	Kim ki chang	*	미술작가
김대수	*	Kim dae soo	*	미술작가
김대열	*	Kim Daeyeoul	*	미술작가
김대원	*	Kim dae won	*	미술작가
김명희	*	Kim myung hee	*	회화
김명희	*	Kim myong hi	*	회화
김문식	*	Kim moon sik	*	미술작가
김미형	*	Kim mi hyung	*	회화
김범	*	Kim beom	*	미술작가
김병기	*	Kim byung ki	*	미술작가
김보희	*	Kim bo hie	*	미술작가
김봉구	*	Kim bong goo	*	미술작가
김봉준	*	Kim bong jun	*	미술작가
김봉태	*	Kim bong tae	*	미술작가
김부자	*	Kim bu ja	*	시각기타
김상구	*	Kim sang ku	*	미술작가
김서봉	*	Kim ser bohng	*	회화
김석	*	Kim suk	*	조각
김선두	*	Kim sun doo	*	미술작가
김선회	*	Kim sun whoe	*	미술작가
김세일	*	Kim se il	*	조각
김승연	*	Kim seung yeon	*	미술작가
김승희	*	Kim seung hee	*	공예
김식	*	Kim shik	*	미술작가
김아영	*	Kim ah young	*	미술작가
김아타	*	Kim a tta	*	미술작가
김안나	*	Kim ahn na	*	미술작가
김애영	*	Kim aie yung	*	미술작가
김영기	*	Kim young kee	*	미술작가
김영원	*	Kim young won	*	미술작가
김영진	*	Kim young jin	*	미술작가
김옥조	*	Kim ok jo	*	시각기타
김옥진	*	Kim ok jin	*	시각기타
김용문	*	Kim yong moon	*	공예
김용식	*	Kim yong sik	*	미술작가
김용철	*	Kim yong chul	*	미술작가
김웅	*	Kim woong	*	미술작가
김원	*	Kim won	*	시각기타
김원숙	*	Kim won sook	*	미술작가
김유선	*	Kim you sun	*	미술작가
김은진	*	Kim eun jin	*	시각기타
김익영	*	Kim yik yung	*	미술작가
김인겸	*	Kim in kyum	*	미술작가
김인경	*	Kim in kyung	*	시각기타
김인순	*	Kim in sun	*	시각기타
김인중	*	Kim en joong	*	미술작가
김일용	*	Kim il yong	*	미술작가
김재관	*	Kim jai kwan	*	미술작가
김정명	*	Kim jung myung	*	미술작가
김정헌	*	Kim jeong heon	*	미술작가
김종하	*	金鐘夏	*	회화
김종학	*	Kim jong hak	*	시각기타
김주현	*	Kim joo hyun	*	미술작가
김주호	*	Kim joo ho	*	조각
김준	*	Kim joon	*	미술작가
김지현	*	Kim ji hyun	*	미술작가
김진관	*	Kim jin kwan	*	미술작가
김진명	*	Kim jin myung	*	미술작가
김진수	*	Kim jin soo	*	시각기타
김진영	*	Kim jin yung	*	미술작가
김차섭	*	金次燮	*	회화
김창겸	*	Kim chang kyum	*	미술작가
김창세	*	Kim chang se	*	시각기타
김창열	*	金昌烈	*	회화
김창희	*	Kim chang hee	*	미술작가
김천영	*	Kim cheon young	*	미술작가
김천일	*	Kim cheon il	*	미술작가
김청정	*	Kim chung jung	*	미술작가
김춘수	*	Kim tschoon su	*	미술작가
김춘옥	*	Kim chun ok	*	시각기타
김태	*	Kim tai	*	미술작가
김태곤	*	Kim tae gon	*	미술작가
김태호	*	Kim tae ho	*	회화
김태호	*	Kim tai ho	*	회화
김학수	*	金學洙	*	회화
김형근	*	金炯菫	*	회화
김형대	*	Kim hyung dae	*	미술작가
김형수	*	金亨洙	*	회화
김혜원	*	Kim hae won	*	미술작가
김호득	*	Kim ho duck	*	미술작가
김호석	*	Kim ho suk	*	미술작가
김홍주	*	Kim hong joo	*	시각기타
김홍희	*	Kim hong hee	*	미술작가
김황록	*	Kim hwang rok	*	미술작가
김효숙	*	Gim hyo sook	*	미술작가
김흥수	*	金興洙	*	회화
나기환	*	Na ki whan	*	시각기타
노원희	*	Noh won hee	*	미술작가
노은님	*	Ro eun nim	*	미술작가
노재승	*	Noh jae seung	*	미술작가
노정란	*	Jung ran Noh	*	회화
도윤희	*	To hyun hee	*	미술작가
레이몬드한	*	Laymond hahn	*	미술작가
류병엽	*	Rhoo byung yup	*	미술작가
류재구	*	Liu jai koo	*	미술작가
문봉선	*	Moon Bong-sun	*	시각기타
문은희	*	文銀姬	*	회화
문인상	*	Moon in sang	*	미술작가
문인수	*	Moon in soo	*	미술작가
문종숙	*	Moon jong sook	*	미술작가
문주	*	Moon joo	*	미술작가
민경갑	*	閔庚甲	*	회화
민경찬	*	Min kyung chan	*	미술작가
민병헌	*	Min byung hun	*	미술작가
민복진	*	閔福鎭	*	조각
민정기	*	Min joung ki	*	미술작가
박경주	*	Park kyung joo	*	공예
박고석	*	Park ko suk	*	미술작가
박광진	*	Park kwang jin	*	미술작가
박기웅	*	Park ki woong	*	미술작가
박남철	*	Park nam cheol	*	미술작가
박노수	*	Park no soo	*	미술작가
박대성	*	Park dae sung	*	미술작가
박돈	*	(朴敦), 본명 박창돈(朴昌敦)	*	회화
박동인	*	Park dong in	*	미술작가
박문종	*	Park moon jong	*	미술작가
박복규	*	Park boc kyoo	*	미술작가
박불똥	*	Park bul ddong	*	회화
박상숙	*	Park sang sook	*	미술작가
박서보	*	朴栖甫, 본명 박재홍(朴在弘)	*	회화
박석원	*	Park suk won	*	미술작가
박선희	*	Park sun hee	*	미술작가
박성환	*	Park sung hwan	*	미술작가
박성희	*	Park sung hee	*	미술작가
박소영	*	Park so young	*	미술작가
박승규	*	Park seung kyu	*	회화
박실	*	Park sil	*	미술작가
박애정	*	Park ad jong	*	미술작가
박영근	*	Park young geun	*	미술작가
박영남	*	Park yung nam	*	미술작가
박영대	*	Park young dae	*	회화
박영숙	*	Park young sook	*	미술작가
박이소	*	Bahc yi so	*	시각기타
박인현	*	Parkinhyun	*	시각기타
박일순	*	Park il soon	*	미술작가
박정애	*	Park jung ae	*	미술작가
박종배	*	Park chong bae	*	시각기타
박충흠	*	Park choong heum	*	미술작가
박항률	*	Park hang ryul	*	미술작가
박헌열	*	Park heon youl	*	미술작가
박혜성	*	Park hye sung	*	시각기타
박홍천	*	Park, HongChun	*	시각기타
박화영	*	Park hwa young	*	미술작가
박훈성	*	Park hoon sung	*	미술작가
배동신	*	Bae dong shin	*	미술작가
배동환	*	Bai dong hwan	*	미술작가
배병우	*	Bae bien u	*	미술작가
배준성	*	Bae joon sung	*	미술작가
배진환	*	Bae jin hwan	*	미술작가
배형식	*	Bae hyung sik	*	미술작가
백남준	*	Paik nam jun	*	미술작가
백문기	*	白文基	*	조각
백순실	*	Baik soon shil	*	미술작가
백철수	*	Paik chul soo	*	미술작가
백태호	*	Paik tai ho	*	미술작가
변시지	*	邊時志	*	회화
사석원	*	Sa suk won	*	회화
서도식	*	Seo do sik	*	미술작가
서세옥	*	Suh se ok	*	미술작가
서승원	*	Suh seung won	*	미술작가
서용선	*	Suh yongsun	*	미술작가
서정국	*	Seo jung kug	*	미술작가
서정태	*	Suh jung tae	*	미술작가
서정희	*	Seo jeong hee	*	미술작가
석난희	*	Suk ran hi	*	미술작가
석영기	*	Soug young ki	*	미술작가
석철주	*	Suk chul joo	*	미술작가
설원기	*	Sul won gi	*	시각기타
성기점	*	Sung kee jeoum	*	미술작가
성백주	*	Sung paik Joo	*	미술작가
성옥희	*	Sung ok hi	*	시각기타
손연칠	*	Son yeon chil	*	미술작가
손인선	*	Son in sun	*	시각기타
손장섭	*	孫壯燮	*	회화
송계일	*	宋桂一	*	회화
송수남	*	宋秀南	*	회화
송수련	*	Song soo ryun	*	미술작가
송영방	*	宋榮邦	*	회화
송필용	*	Song phil yong	*	미술작가
신산옥	*	Shin san ok	*	미술작가
신상호	*	Shin sang ho	*	시각기타
신수희	*	Shin soo hee	*	미술작가
신영상	*	辛永常	*	회화
신옥주	*	Shin Ok Joo	*	시각기타
신장식	*	Shin jang sik	*	시각기타
신현중	*	Shin hyun jung	*	시각기타
신혜경	*	Shin hye kyung	*	회화
심경자	*	沈敬子	*	회화
심문섭	*	Shim moon seup	*	미술작가
심영철	*	Shim young chul	*	미술작가
심정수	*	Shim jung soo	*	시각기타
심철웅	*	Sim cheol woong	*	미술작가
심현주	*	Shim hyun joo	*	미술작가
심현희	*	Shim hyun hee	*	미술작가
안규철	*	Ahn kyu chul	*	시각기타
안동숙	*	安東淑	*	회화
안병석	*	Ahn byeong seok	*	미술작가
안성금	*	An seong keum	*	시각기타
안수진	*	Ahn soo jin	*	시각기타
안종연	*	Ahn jong yuen	*	미술작가
안창홍	*	Ahn chang hong	*	미술작가
안필연	*	Ahn pil yun	*	미술작가
양주혜	*	Yang ju hae	*	미술작가
양화선	*	Yang hwa sun	*	미술작가
엄정순	*	Oum jeong soon	*	미술작가
엄정윤	*	嚴丁潤	*	공예
엄태정	*	Um tai jung	*	미술작가
염은경	*	Yeom eun kyong	*	시각기타
오경화	*	Oh kyung hwa	*	미술작가
오경환	*	Oh kyung hwan	*	미술작가
오경환	*	Oh kyung hwan	*	시각기타
오광섭	*	Oh kwang seob	*	시각기타
오낭자	*	Oh nang ja	*	시각기타
오상길	*	Oh sang ghil	*	미술작가
오상욱	*	Oh sang wook	*	미술작가
오수환	*	Oh su fan	*	미술작가
오숙환	*	Oh sook whan	*	미술작가
오순희	*	Oh soon hee	*	미술작가
오승우	*	吳承雨	*	회화
오승윤	*	O syng yoon	*	시각기타
오용길	*	Oh yong kil	*	미술작가
오원배	*	Oh won bae	*	미술작가
오이량   吳二良	*	yiryang Oh	*	시각기타
오치균	*	Oh chi gyun	*	미술작가
오태학	*	吳泰鶴	*	회화
오형근	*	Oh hyoung kuhn	*	미술작가
왕경애	*	Wang kyung ae	*	미술작가
우관호	*	Woo kwan ho	*	미술작가
우상기	*	Woo sang ki	*	미술작가
우순옥	*	U sun ok	*	미술작가
우제길	*	Woo jae gil	*	미술작가
원경환	*	Won kyung hwan	*	미술작가
원문자	*	Won moon ja	*	미술작가
원인종	*	Won in jong	*	미술작가
유근택	*	Yoo geun taek	*	미술작가
유리지	*	Yoo li zzy	*	미술작가
유병훈	*	Yoo byeong hoon	*	미술작가
유성일	*	Yu sung il	*	미술작가
유영교	*	Yoo young kyo	*	미술작가
유영국	*	Yoo young kuk	*	미술작가
유영주	*	You young joo	*	시각기타
유철연	*	Yu cheol yeon	*	미술작가
유현미	*	Yoo hyun mi	*	미술작가
유휴열	*	Ryu hu yeol	*	미술작가
유희영	*	Ryu hee young	*	미술작가
육근병	*	Yook keun byung	*	미술작가
육태진	*	Yook tae jin	*	미술작가
윤명로	*	尹明老	*	회화
윤석구	*	Yoon seok koo	*	미술작가
윤석남	*	Yun suk nam	*	미술작가
윤영석	*	Yoon yong seok	*	미술작가
윤영자	*	尹英子	*	조각
윤중식	*	Yun jung sik	*	미술작가
윤지해	*	Youn ji hae	*	미술작가
윤형근	*	Yun hyong keun	*	미술작가
이강소	*	Lee kang so	*	미술작가
이강우	*	Lee kang woo	*	미술작가
이건용	*	Lee kun yong	*	시각기타
이규선	*	Lee kyu sun	*	미술작가
이기봉	*	Rhee ki bong	*	시각기타
이기칠	*	Yi gee chil	*	미술작가
이동기	*	Lee dongi	*	미술작가
이동엽	*	Lee dong youb	*	미술작가
이두식	*	Lee doo shik	*	미술작가
이명미	*	Lee myung mi	*	미술작가
이민주	*	MinJoo Lee	*	미술작가
이봉열	*	Lee bong real	*	미술작가
이상명	*	Lee sang myung	*	미술작가
이상일	*	Lee sang il	*	사진
이상현	*	Lee sang hyun	*	미술작가
이석주	*	Lee suk ju	*	미술작가
이선우	*	Lee sun woo	*	미술작가
이성근	*	Lee sung keun	*	시각기타
이성순	*	Lee sung soon	*	미술작가
이성자	*	Seundja Rhee	*	회화
이세득	*	Lee se duk	*	회화
이수재	*	Lee soo jai	*	시각기타
이수종	*	Ree soo jong	*	미술작가
이수홍	*	Lee soo hong	*	미술작가
이숙자	*	李淑子	*	회화
이승택	*	Lee seung teak	*	조각
이승하	*	Lee seung ha	*	시각기타
이신자	*	李信子	*	공예
이양원	*	Lee yang won	*	시각기타
이열모	*	Lee yul mo	*	시각기타
이영배	*	Lee young bae	*	시각기타
이영수	*	Lee young su	*	미술작가
이영학	*	Lee young hak	*	미술작가
이왈종	*	Lee wal jong	*	회화
이용백	*	Lee yong baek	*	미술작가
이우환	*	Lee u fan	*	미술작가
이원좌	*	Lee won jwa	*	미술작가
이유태	*	Lee yu tae	*	미술작가
이윰	*	Ium	*	미술작가
이인실	*	李仁實	*	회화
이인현	*	Lee in hyeon	*	미술작가
이일호	*	Lee il ho	*	미술작가
이재삼	*	Lee jae sam	*	미술작가
이재효	*	Lee jae hyo	*	미술작가
이정신	*	Lee chung shin	*	미술작가
이정열	*	Lee jeong yeol	*	미술작가
이정지	*	Lee chung ji	*	시각기타
이정진	*	Lee jung jin	*	미술작가
이종각	*	Lee jong gak	*	미술작가
이종구	*	Lee jong gu	*	미술작가
이종목	*	Lee jong mok	*	미술작가
이종무	*	Lee jong mu	*	미술작가
이종빈	*	Lee jong bin	*	미술작가
이종상	*	李鐘祥	*	회화
이준	*	Lee, Joon	*	미술작가
이준목	*	Lee jun mok	*	시각기타
이철량	*	Lee cheol ryang	*	미술작가
이철주	*	Lee cheol joo	*	미술작가
이형우	*	Lee hyung woo	*	미술작가
이호철	*	Lee ho chul	*	시각기타
이흥덕	*	Lee heung duk	*	시각기타
이희중	*	Lee hee jung	*	미술작가
임동락	*	Lim dong lak	*	미술작가
임무근	*	Lim moo keun	*	미술작가
임송자	*	Rim song ja	*	미술작가
임송희	*	林頌羲	*	회화
임영균	*	Lim young kyun	*	미술작가
임영길	*	Yim young kil	*	미술작가
임옥상	*	Lim ok sang	*	미술작가
임응식	*	Limb eung sik	*	시각기타
임충섭	*	Lim choong sup	*	미술작가
임홍순	*	Lim hong sun	*	미술작가
임효	*	Rim hyo	*	미술작가
장두건	*	張斗建	*	회화
장리석	*	張利錫	*	회화
장상의	*	張相宜	*	회화
장선영	*	Chang sun young	*	미술작가
장수홍	*	Jahng soo hong	*	미술작가
장순업	*	Chang soon up	*	미술작가
장식	*	Chang sik	*	미술작가
장우성	*	Chang woo sung	*	미술작가
장욱희	*	Jang wookie	*	미술작가
장진	*	Jang jin	*	미술작가
장화진	*	Chang hwa jin	*	미술작가
전광영	*	Chun kwang young	*	미술작가
전뢰진	*	Joen roi jin	*	미술작가
전성우	*	全晟雨	*	회화
전수천	*	Jheon soo cheon	*	미술작가
전재은	*	Jeon jae eun	*	미술작가
전준	*	Chon joon	*	미술작가
전준엽	*	Chun jun yeup	*	미술작가
전항섭	*	Jeon hang sub	*	시각기타
전혁림	*	全爀林	*	회화
정경연	*	Chung kyung yeun	*	미술작가
정관모	*	Chung kwan mo	*	미술작가
정광호	*	Cheong kwang ho	*	시각기타
정국택	*	Chung kuk taek	*	미술작가
정명희	*	Jeong myeong hee	*	미술작가
정문규	*	Chung mun kyu	*	미술작가
정미조	*	Jeong mi jo	*	미술작가
정보원	*	Chung bo won	*	미술작가
정복수	*	Jung bok soo	*	미술작가
정상화	*	Chung sang hwa	*	미술작가
정서영	*	Chung seo young	*	미술작가
정승운	*	Chung seung un	*	미술작가
정일	*	Chung il	*	시각기타
정재철	*	Joung jae choul	*	미술작가
정점식	*	鄭點植	*	회화
정정희	*	Chung chung hee	*	미술작가
정종미	*	Jeong jong mee	*	시각기타
정종해	*	Chung chu ha	*	미술작가
정주하	*	Chung chang sup	*	미술작가
정창섭	*	Jung tak young	*	미술작가
정탁영	*	鄭晫永	*	회화
정하경	*	Chung ha kyung	*	미술작가
정현	*	Chung hyun	*	미술작가
정현도	*	Jeong hyun do	*	미술작가
제여란	*	Je yeo ran	*	미술작가
조경아	*	Cho kyung a	*	미술작가
조기주	*	Cho khee joo	*	시각기타
조남붕	*	Cho nam boong	*	미술작가
조덕현	*	Cho duck hyun	*	미술작가
조문자	*	Cho moon ja	*	미술작가
조성묵	*	Cho sung mook	*	미술작가
조순호	*	Cho soon ho	*	미술작가
조용익 (개명 전 : 조태하)	*	趙容翊 (개명 전 : 趙泰河)	*	회화
조재익	*	Cho jae ik	*	미술작가
조정현	*	Cho chung hyun	*	미술작가
조평휘	*	趙平彙	*	회화
주민숙	*	Joo min suk	*	미술작가
주태석	*	Ju tae seok	*	시각기타
지석철	*	Ji seok cheol	*	미술작가
진송자	*	Jin song ja	*	미술작가
진영선	*	Jin young sun	*	미술작가
진옥선	*	Jin ok sun	*	미술작가
차계남	*	Cha kea nam	*	미술작가
차명희	*	Cha myung hi	*	미술작가
차순실	*	Cha soon shil	*	시각기타
차영규	*	Cha young kyu	*	미술작가
차우희	*	Chao u hi	*	미술작가
채미현	*	Chae mi hyun	*	미술작가
천경자	*	Chun kyung ja	*	미술작가
최경한	*	Choi kyung han	*	시각기타
최광호	*	Choi kwang ho	*	시각기타
최기원	*	Choi ki won	*	미술작가
최만린	*	Choi man lin	*	미술작가
최민식	*	Choi min sick	*	미술작가
최병상	*	Choi byeong sang	*	미술작가
최병훈	*	Choi byung hoon	*	미술작가
최승천	*	Choi seung cheon	*	미술작가
최쌍중	*	Choi ssang joong	*	미술작가
최영훈	*	Choe young hoon	*	미술작가
최우람	*	Choe u ram	*	미술작가
최인선	*	Choi in sun	*	미술작가
최정화	*	Choi jung hwa	*	미술작가
최종태	*	崔鍾泰	*	조각
최진욱	*	Choi, Gene-Uk	*	시각기타
하동철	*	Ha dong chul	*	미술작가
하수경	*	Ha soo kyung	*	시각기타
하정민	*	Ha jeong min	*	시각기타
하종현	*	Ha chong hyun	*	시각기타
하태진	*	河泰瑨	*	회화
한기주	*	Han ki joo	*	미술작가
한기창	*	Han ki chang	*	시각기타
한길홍	*	Han gil hong	*	시각기타
한만영	*	Han man young	*	회화
한애규	*	Hahn ai kyu	*	미술작가
한영섭	*	Han young sup	*	시각기타
한운성	*	Han un sung	*	미술작가
한진만	*	Han jin man	*	미술작가
한진섭	*	Han jin sub	*	미술작가
한풍렬	*	Han poong ryul	*	미술작가
함섭	*	Ham sup	*	시각기타
함진	*	Ham jin	*	미술작가
허계	*	Heo gye	*	미술작가
허진	*	Hur jin	*	미술작가
허황	*	Hur hwang	*	미술작가
형진식	*	Hyung jin sik	*	시각기타
홍미선	*	Hong mi sun	*	시각기타
홍석창	*	洪石蒼, 본명 홍숙호(洪璹鎬)	*	회화
홍성담	*	Hong sung dam	*	미술작가
홍성도	*	Hong sung do	*	시각기타
홍성민	*	Hong sung min	*	시각기타
홍수자	*	Hong su ja	*	미술작가
홍순모	*	Hong soon mo	*	시각기타
홍순주	*	Hong soon joo	*	미술작가
홍순태	*	Hong soon tai	*	미술작가
홍승남	*	Hong, Seung-Nam	*	시각기타
홍승혜	*	Hong seung hye	*	미술작가
홍정희	*	Hong jung hee	*	미술작가
홍종명	*	Hong chong myung	*	미술작가
홍현숙	*	Hong hyun sook	*	시각기타
황규백	*	Hwang kyu baik	*	시각기타
황영성	*	Hwang young sung	*	미술작가
황용엽	*	Hwang yong yop	*	미술작가
황용진	*	Hwang yong jin	*	미술작가
황유엽	*	Hwang you yop	*	시각기타
황인기	*	Whang in kie	*	미술작가
황종례	*	黃鍾禮	*	공예
황주리	*	Hwang ju lie	*	미술작가
황창배	*	Hwang chang bae	*	시각기타
황현수	*	Hwang hyun soo	*	미술작가"""

"""

from posts.forms import *
artists = list(strings.split("\n"))
for artist in artists:
    name_ko, name_en, category = artist.split('*')
    data = {
        'name_ko': name_ko.strip(),
        'name_en': name_en.strip(),
        'category': category.strip(),
    }
    form = ArtistForm(data=data)
    if form.is_valid():
        form.save()
    else:
        print(" message :", form.is_bound, form.errors)

"""
