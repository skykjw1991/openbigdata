import urllib.request
from bs4 import BeautifulSoup

html= """
<html>
            <tbody>
				<tr><td colspan="8" class="blank01"></td></tr>
				<!-- 예제
				<tr>
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>
					<td class="title"><a href="#">트랜스포머</a></td>
					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10"></td>
					<td class="range ac">7</td>
				</tr>
				-->

				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=162249" title="램페이지">램페이지</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" alt="02" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=136315" title="어벤져스: 인피니티 워">어벤져스: 인피니티 워</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r03.gif" alt="03" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=173653" title="그날, 바다">그날, 바다</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r04.gif" alt="04" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=158555" title="나를 기억해">나를 기억해</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r05.gif" alt="05" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=168011" title="콰이어트 플레이스">콰이어트 플레이스</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r06.gif" alt="06" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=136898" title="레디 플레이어 원">레디 플레이어 원</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r07.gif" alt="07" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=142739" title="바람 바람 바람">바람 바람 바람</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r08.gif" alt="08" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=172454" title="곤지암">곤지암</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>

						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r09.gif" alt="09" width="14" height="13"></td>




					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=168036" title="크리미널 스쿼드">크리미널 스쿼드</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>


					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r10.gif" alt="010" width="14" height="13"></td>



					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=154667" title="덕구">덕구</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>


						<tr><td colspan="8" class="line01"></td></tr>


				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g11.gif" alt="11" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=125494" title="퍼시픽 림: 업라이징">퍼시픽 림: 업라이징</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g12.gif" alt="12" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159311" title="소공녀">소공녀</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g13.gif" alt="13" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=158178" title="독전">독전</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g14.gif" alt="14" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=85578" title="7년의 밤">7년의 밤</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g15.gif" alt="15" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159864" title="당신의 부탁">당신의 부탁</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g16.gif" alt="16" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=151744" title="레드 스패로">레드 스패로</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g17.gif" alt="17" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=158628" title="몬태나">몬태나</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g18.gif" alt="18" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=169347" title="챔피언">챔피언</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g19.gif" alt="19" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=168298" title="지금 만나러 갑니다">지금 만나러 갑니다</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g20.gif" alt="20" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=157974" title="살인소설">살인소설</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">4</td>


				</tr>


						<tr><td colspan="8" class="line01"></td></tr>


				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g21.gif" alt="21" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=151241" title="머니백">머니백</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g22.gif" alt="22" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=165026" title="사라진 밤">사라진 밤</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g23.gif" alt="23" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=158885" title="콜 미 바이 유어 네임">콜 미 바이 유어 네임</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g24.gif" alt="24" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=158611" title="레이디 버드">레이디 버드</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g25.gif" alt="25" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=39636" title="지금, 만나러 갑니다">지금, 만나러 갑니다</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g26.gif" alt="26" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=152663" title="블리딩 스틸">블리딩 스틸</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g27.gif" alt="27" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=168037" title="12 솔져스">12 솔져스</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g28.gif" alt="28" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=137326" title="블랙 팬서">블랙 팬서</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g29.gif" alt="29" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=149236" title="데드풀 2">데드풀 2</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g30.gif" alt="30" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=157243" title="당갈">당갈</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">6</td>


				</tr>


						<tr><td colspan="8" class="line01"></td></tr>


				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g31.gif" alt="31" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=154449" title="리틀 포레스트">리틀 포레스트</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g32.gif" alt="32" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=170139" title="마징가 Z: 인피니티">마징가 Z: 인피니티</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g33.gif" alt="33" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=171403" title="정글번치: 최강 악당의 등장">정글번치: 최강 악당의 등장</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g34.gif" alt="34" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=152655" title="달링">달링</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">6</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g35.gif" alt="35" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159731" title="한낮의 유성">한낮의 유성</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g36.gif" alt="36" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=154598" title="50가지 그림자: 해방">50가지 그림자: 해방</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g37.gif" alt="37" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=155263" title="버닝">버닝</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g38.gif" alt="38" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=142250" title="수성못">수성못</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g39.gif" alt="39" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159827" title="클레어의 카메라">클레어의 카메라</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g40.gif" alt="40" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159855" title="영웅본색4">영웅본색4</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">1</td>


				</tr>


						<tr><td colspan="8" class="line01"></td></tr>


				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g41.gif" alt="41" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=164974" title="원죄">원죄</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">6</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g42.gif" alt="42" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=87309" title="라이프 오브 파이">라이프 오브 파이</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">5</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g43.gif" alt="43" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=165347" title="렛 더 선샤인 인">렛 더 선샤인 인</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">15</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g44.gif" alt="44" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=27219" title="박하사탕">박하사탕</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">16</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g45.gif" alt="45" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=149248" title="메이즈 러너: 데스 큐어">메이즈 러너: 데스 큐어</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">3</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g46.gif" alt="46" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=154206" title="콜럼버스">콜럼버스</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" alt="na" width="7" height="10" class="arrow"></td>
					<td class="range ac">0</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g47.gif" alt="47" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=164719" title="플로리다 프로젝트">플로리다 프로젝트</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">2</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g48.gif" alt="48" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=86867" title="퍼시픽 림">퍼시픽 림</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">7</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g49.gif" alt="49" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=159366" title="호랑이보다 무서운 겨울손님">호랑이보다 무서운 겨울손님</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow"></td>
					<td class="range ac">6</td>


				</tr>



				<tr>



						<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>


					<td class="title">
						<div class="tit3">
							<a href="/movie/bi/mi/basic.nhn?code=152616" title="47 미터">47 미터</a>
						</div>
					</td>
					<!-- 평점순일 때 평점 추가하기  -->

					<!----------------------------------------->

					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_up_1.gif" alt="up" width="7" height="10" class="arrow"></td>
					<td class="range ac">9</td>


				</tr>



					<tr><td colspan="8" class="blank01"></td></tr>
			</tbody>
</html>"""

soup=BeautifulSoup(html,'html.parser')

tags = soup.find_all('a')
tag = soup.find_all('img')
range = soup.td
n=0

for titles in tags:
    attribute = tag[n].attrs['alt']
    attribute1 = tag[n+1].attrs['alt']
    attribute2 = range.text
    n = n + 2
    print(attribute)
    print(titles.text)
    print(attribute1)
    print(attribute2)
    print("\n")

# print(tag)
# print(tag.name)
# print(tag.attrs)
#
# print(tag.string)
#
# print("\ntag.text")
# print(tag.text)