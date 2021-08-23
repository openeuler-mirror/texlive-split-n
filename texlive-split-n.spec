%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-n
Version:        %{tl_version}
Release:        25
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexconfig.tar.xz
Source0220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-fonts.tar.xz
Source0221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-fonts.doc.tar.xz
Source0223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lambda.tar.xz
Source1363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-alt-getopt.tar.xz
Source1364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-alt-getopt.doc.tar.xz
Source1405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxmisc.tar.xz
Source1482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logreq.tar.xz
Source1483:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logreq.doc.tar.xz
Source1665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lm.tar.xz
Source1666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lm.doc.tar.xz
Source1668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lm-math.tar.xz
Source1669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lm-math.doc.tar.xz
Source1928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lato.tar.xz
Source1929:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lato.doc.tar.xz
Source1931:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lfb.tar.xz
Source1932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lfb.doc.tar.xz
Source1933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertine.tar.xz
Source1934:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertine.doc.tar.xz
Source1935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librebaskerville.tar.xz
Source1936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librebaskerville.doc.tar.xz
Source1937:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librecaslon.tar.xz
Source1938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librecaslon.doc.tar.xz
Source1939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libris.tar.xz
Source1940:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libris.doc.tar.xz
Source1942:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linearA.tar.xz
Source1943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linearA.doc.tar.xz
Source1945:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lobster2.tar.xz
Source1946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lobster2.doc.tar.xz
Source1947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lxfonts.tar.xz
Source1948:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lxfonts.doc.tar.xz
Source1950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ly1.tar.xz
Source1951:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ly1.doc.tar.xz
Source2229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labyrinth.tar.xz
Source2230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labyrinth.doc.tar.xz
Source2231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logicpuzzle.tar.xz
Source2232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logicpuzzle.doc.tar.xz
Source2296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lambda-lists.tar.xz
Source2297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lambda-lists.doc.tar.xz
Source2298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/langcode.tar.xz
Source2299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/langcode.doc.tar.xz
Source2301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lecturer.tar.xz
Source2302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lecturer.doc.tar.xz
Source2303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librarian.tar.xz
Source2304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librarian.doc.tar.xz
Source2413:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ledmac.tar.xz
Source2414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ledmac.doc.tar.xz
Source2416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leipzig.tar.xz
Source2417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leipzig.doc.tar.xz
Source2421:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lexref.tar.xz
Source2422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lexref.doc.tar.xz
Source2423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linguex.tar.xz
Source2424:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linguex.doc.tar.xz
Source2425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/liturg.tar.xz
Source2426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/liturg.doc.tar.xz
Source2501:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-persian.doc.tar.xz
Source2522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-notes-zh-cn.doc.tar.xz
Source2523:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-chinese.doc.tar.xz
Source2562:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcyw.tar.xz
Source2563:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcyw.doc.tar.xz
Source2565:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lh.tar.xz
Source2566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lh.doc.tar.xz
Source2568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lhcyr.tar.xz
Source2570:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-bulgarian.doc.tar.xz
Source2571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-mongol.doc.tar.xz
Source2572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-russian.doc.tar.xz
Source2573:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-ukr.doc.tar.xz
Source2604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-czech.doc.tar.xz
Source2605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-slovak.doc.tar.xz
Source2623:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2tabu-english.doc.tar.xz
Source2624:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-brochure.doc.tar.xz
Source2625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-course.doc.tar.xz
Source2626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-doc-ptr.doc.tar.xz
Source2627:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-graphics-companion.doc.tar.xz
Source2628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-veryshortguide.doc.tar.xz
Source2629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-web-companion.doc.tar.xz
Source2630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2e-help-texinfo.tar.xz
Source2631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2e-help-texinfo.doc.tar.xz
Source2632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex4wp.doc.tar.xz
Source2633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexcheat.doc.tar.xz
Source2634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexcourse-rug.doc.tar.xz
Source2635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexfileinfo-pkgs.tar.xz
Source2636:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexfileinfo-pkgs.doc.tar.xz
Source2638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-english.doc.tar.xz
Source2694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lithuanian.tar.xz
Source2695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lithuanian.doc.tar.xz
Source2696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-dutch.doc.tar.xz
Source2697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-finnish.doc.tar.xz
Source2698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-slovenian.doc.tar.xz
Source2699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-turkish.doc.tar.xz
Source2724:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2tabu-french.doc.tar.xz
Source2725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-french.doc.tar.xz
Source2765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2picfaq.doc.tar.xz
Source2766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2tabu.doc.tar.xz
Source2767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-bib-ex.doc.tar.xz
Source2768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-referenz.doc.tar.xz
Source2769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-tabellen.doc.tar.xz
Source2770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexcheat-de.doc.tar.xz
Source2771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-german.doc.tar.xz
Source2772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-doc-de.doc.tar.xz
Source2820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/levy.tar.xz
Source2821:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/levy.doc.tar.xz
Source2822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lgreek.tar.xz
Source2823:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lgreek.doc.tar.xz
Source2864:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2tabu-italian.doc.tar.xz
Source2865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex4wp-it.doc.tar.xz
Source2866:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/layaureo.tar.xz
Source2867:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/layaureo.doc.tar.xz
Source2869:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-italian.doc.tar.xz
Source2891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-japanese.doc.tar.xz
Source2892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexja.tar.xz
Source2893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexja.doc.tar.xz
Source2929:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-korean.doc.tar.xz
Source2943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-thai.doc.tar.xz
Source2944:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-vietnamese.doc.tar.xz
Source2953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-polish.doc.tar.xz
Source2979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexcheat-ptbr.doc.tar.xz
Source2980:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-portuguese.doc.tar.xz
Source2989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l2tabu-spanish.doc.tar.xz
Source2990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2e-help-texinfo-spanish.tar.xz
Source2991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2e-help-texinfo-spanish.doc.tar.xz
Source2992:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexcheat-esmx.doc.tar.xz
Source2993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-spanish.doc.tar.xz
Source3027:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3kernel.tar.xz
Source3028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3kernel.doc.tar.xz
Source3030:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3packages.tar.xz
Source3031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3packages.doc.tar.xz
Source3041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3experimental.tar.xz
Source3042:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3experimental.doc.tar.xz
Source3044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lineno.tar.xz
Source3045:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lineno.doc.tar.xz
Source3047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listings.tar.xz
Source3048:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listings.doc.tar.xz
Source3192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lapdf.tar.xz
Source3193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lapdf.doc.tar.xz
Source3194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-make.tar.xz
Source3195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-make.doc.tar.xz
Source3197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lpic.tar.xz
Source3198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lpic.doc.tar.xz
Source4395:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labbook.tar.xz
Source4396:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labbook.doc.tar.xz
Source4401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labels.tar.xz
Source4402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labels.doc.tar.xz
Source4404:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lastpackage.tar.xz
Source4405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lastpackage.doc.tar.xz
Source4407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lastpage.tar.xz
Source4408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lastpage.doc.tar.xz
Source4410:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexdemo.tar.xz
Source4411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexdemo.doc.tar.xz
Source4413:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/layouts.tar.xz
Source4414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/layouts.doc.tar.xz
Source4416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lazylist.tar.xz
Source4417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lazylist.doc.tar.xz
Source4418:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcd.tar.xz
Source4419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcd.doc.tar.xz
Source4421:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcg.tar.xz
Source4422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcg.doc.tar.xz
Source4424:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leading.tar.xz
Source4425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leading.doc.tar.xz
Source4427:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leaflet.tar.xz
Source4428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leaflet.doc.tar.xz
Source4430:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leftidx.tar.xz
Source4431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leftidx.doc.tar.xz
Source4433:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lengthconvert.tar.xz
Source4434:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lengthconvert.doc.tar.xz
Source4436:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lettre.tar.xz
Source4437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lettre.doc.tar.xz
Source4438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lettrine.tar.xz
Source4439:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lettrine.doc.tar.xz
Source4441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lewis.tar.xz
Source4442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lewis.doc.tar.xz
Source4443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lhelp.tar.xz
Source4444:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lhelp.doc.tar.xz
Source4446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libgreek.tar.xz
Source4447:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libgreek.doc.tar.xz
Source4449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/limap.tar.xz
Source4451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linegoal.tar.xz
Source4452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linegoal.doc.tar.xz
Source4454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lipsum.tar.xz
Source4455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lipsum.doc.tar.xz
Source4457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lisp-on-tex.tar.xz
Source4458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lisp-on-tex.doc.tar.xz
Source4459:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listing.tar.xz
Source4460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listing.doc.tar.xz
Source4461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listlbls.tar.xz
Source4462:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listlbls.doc.tar.xz
Source4464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listliketab.tar.xz
Source4465:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listliketab.doc.tar.xz
Source4467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listofsymbols.tar.xz
Source4468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listofsymbols.doc.tar.xz
Source4470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lkproof.tar.xz
Source4471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lkproof.doc.tar.xz
Source4472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lmake.tar.xz
Source4473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lmake.doc.tar.xz
Source4475:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/locality.tar.xz
Source4476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/locality.doc.tar.xz
Source4478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/localloc.tar.xz
Source4479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/localloc.doc.tar.xz
Source4481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logbox.tar.xz
Source4482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logbox.doc.tar.xz
Source4484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logical-markup-utils.tar.xz
Source4485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logical-markup-utils.doc.tar.xz
Source4486:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logpap.tar.xz
Source4487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logpap.doc.tar.xz
Source4489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longfigure.tar.xz
Source4490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longfigure.doc.tar.xz
Source4492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longnamefilelist.tar.xz
Source4493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longnamefilelist.doc.tar.xz
Source4495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/loops.tar.xz
Source4496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/loops.doc.tar.xz
Source4497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lsc.tar.xz
Source4498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lsc.doc.tar.xz
Source4499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lstaddons.tar.xz
Source4500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lstaddons.doc.tar.xz
Source4502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lt3graph.tar.xz
Source4503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lt3graph.doc.tar.xz
Source4504:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltablex.tar.xz
Source4505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltablex.doc.tar.xz
Source4506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltabptch.tar.xz
Source4507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltabptch.doc.tar.xz
Source4508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxdockit.tar.xz
Source4509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxdockit.doc.tar.xz
Source4510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxindex.tar.xz
Source4511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxindex.doc.tar.xz
Source4513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxkeys.tar.xz
Source4514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxkeys.doc.tar.xz
Source4515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxnew.tar.xz
Source4516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxnew.doc.tar.xz
Source4518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxtools.tar.xz
Source4519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxtools.doc.tar.xz
Source5759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-check-hyphen.tar.xz
Source5760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-check-hyphen.doc.tar.xz
Source5761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-visual-debug.tar.xz
Source5762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua-visual-debug.doc.tar.xz
Source5765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luabibentry.tar.xz
Source5766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luabibentry.doc.tar.xz
Source5768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luabidi.tar.xz
Source5769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luabidi.doc.tar.xz
Source5770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luacode.tar.xz
Source5771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luacode.doc.tar.xz
Source5773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaindex.tar.xz
Source5774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaindex.doc.tar.xz
Source5776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luainputenc.tar.xz
Source5777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luainputenc.doc.tar.xz
Source5779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaintro.doc.tar.xz
Source5780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-doc.doc.tar.xz
Source5782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-math.tar.xz
Source5783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-math.doc.tar.xz
Source5785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualibs.tar.xz
Source5786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualibs.doc.tar.xz
Source5788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luamplib.tar.xz
Source5789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luamplib.doc.tar.xz
Source5794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luasseq.tar.xz
Source5795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luasseq.doc.tar.xz
Source5797:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexbase.tar.xz
Source5798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexbase.doc.tar.xz
Source5800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexko.tar.xz
Source5801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatexko.doc.tar.xz
Source5802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatextra.tar.xz
Source5803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatextra.doc.tar.xz
Source5805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatodonotes.tar.xz
Source5806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatodonotes.doc.tar.xz
Source5808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaxml.tar.xz
Source5809:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaxml.doc.tar.xz
Source5857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logicproof.tar.xz
Source5858:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/logicproof.doc.tar.xz
Source5860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lpform.tar.xz
Source5861:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lpform.doc.tar.xz
Source5862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lplfitch.tar.xz
Source5863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lplfitch.doc.tar.xz
Source5973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexmp.tar.xz
Source5974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexmp.doc.tar.xz
Source6037:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leadsheets.tar.xz
Source6038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/leadsheets.doc.tar.xz
Source6425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lps.tar.xz
Source6426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lps.doc.tar.xz
Source7398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/langsci.tar.xz
Source7399:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/langsci.doc.tar.xz
Source7400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2e-help-texinfo-fr.doc.tar.xz
Source7401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-bib2-ex.doc.tar.xz
Source7402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-tds.doc.tar.xz
Source7404:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinegc.tar.xz
Source7405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinegc.doc.tar.xz
Source7406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinus.tar.xz
Source7407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinus.doc.tar.xz
Source7408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinust1math.tar.xz
Source7409:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinust1math.doc.tar.xz
Source7410:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librebodoni.tar.xz
Source7411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/librebodoni.doc.tar.xz
Source7412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linop.tar.xz
Source7413:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/linop.doc.tar.xz
Source7414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longfbox.tar.xz
Source7415:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longfbox.doc.tar.xz
Source7416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lroundrect.tar.xz
Source7417:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lroundrect.doc.tar.xz
Source7419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lstbayes.tar.xz
Source7420:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lstbayes.doc.tar.xz
Source7422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatex85.tar.xz
Source7423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatex85.doc.tar.xz
Source7596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lshort-estonian.doc.tar.xz
Source7615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listofitems.tar.xz
Source7616:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listofitems.doc.tar.xz
Source7808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ladder.tar.xz
Source7809:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ladder.doc.tar.xz
Source7810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-mr.doc.tar.xz
Source7813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-refsheet.doc.tar.xz
Source7816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexbangla.tar.xz
Source7817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexbangla.doc.tar.xz
Source7818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexbug.tar.xz
Source7819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexbug.doc.tar.xz
Source7820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexgit.tar.xz
Source7821:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexgit.doc.tar.xz
Source7824:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/limecv.tar.xz
Source7825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/limecv.doc.tar.xz
Source7826:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ling-macros.tar.xz
Source7827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ling-macros.doc.tar.xz
Source7828:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lion-msc.tar.xz
Source7829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lion-msc.doc.tar.xz
Source7830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lni.tar.xz
Source7831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lni.doc.tar.xz
Source7832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltb2bib.tar.xz
Source7833:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltb2bib.doc.tar.xz
Source7834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luahyphenrules.tar.xz
Source7835:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luahyphenrules.doc.tar.xz
Source7836:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luamesh.tar.xz
Source7837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luamesh.doc.tar.xz
Source7838:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luapackageloader.tar.xz
Source7839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luapackageloader.doc.tar.xz
Source8188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labelschanged.tar.xz
Source8189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/labelschanged.doc.tar.xz
Source8190:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-via-exemplos.tar.xz
Source8191:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-via-exemplos.doc.tar.xz
Source8192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lccaps.tar.xz
Source8193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lccaps.doc.tar.xz
Source8194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinus-otf.tar.xz
Source8195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/libertinus-otf.doc.tar.xz
Source8196:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/llncsconf.tar.xz
Source8197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/llncsconf.doc.tar.xz
Source8198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longdivision.tar.xz
Source8199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/longdivision.doc.tar.xz
Source8202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-truncate.tar.xz
Source8203:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lualatex-truncate.doc.tar.xz
Source8206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luavlna.tar.xz
Source8207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luavlna.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-lua-alt-getopt
Provides:       tex-lua-alt-getopt = %{tl_version}
License:        MIT
Summary:        Process application arguments the same way as getopt_long
Version:        svn29349.0.7.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-lua-alt-getopt
lua_altgetopt is a MIT-licensed module for Lua, for processing
application arguments in the same way as BSD/GNU getopt_long(3)
functions do. This module is made available for lua script
writers to have consistent command line parsing routines.

%package -n texlive-lua-alt-getopt-doc
Summary:        Documentation for lua-alt-getopt
Version:        svn29349.0.7.0

Provides:       tex-lua-alt-getopt-doc
AutoReqProv:    No

%description -n texlive-lua-alt-getopt-doc
Documentation for lua-alt-getopt

%package -n texlive-ltxmisc
Provides:       tex-ltxmisc = %{tl_version}
License:        Public Domain
Summary:        Miscellaneous LaTeX packages, etc
Version:        svn21927.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makeidx.sty), tex(graphicx.sty), tex(minitoc.sty), tex(beton.sty)
Requires:       tex(euler.sty), tex(calc.sty), tex(natbib.sty), tex(array.sty)
Requires:       tex(pifont.sty)
Provides:       tex(abstbook.cls) = %{tl_version}, tex(beletter.cls) = %{tl_version}
Provides:       tex(bibcheck.sty) = %{tl_version}, tex(concrete.sty) = %{tl_version}
Provides:       tex(flashcard.cls) = %{tl_version}, tex(iagproc.cls) = %{tl_version}
Provides:       tex(linsys.sty) = %{tl_version}, tex(mitpress.sty) = %{tl_version}
Provides:       tex(thrmappendix.sty) = %{tl_version}, tex(topcapt.sty) = %{tl_version}
Provides:       tex(vrbexin.sty) = %{tl_version}

%description -n texlive-ltxmisc
ltxmisc package

%package -n texlive-logreq
Provides:       tex-logreq = %{tl_version}
License:        LPPL 1.3
Summary:        Support for automation of the LaTeX workflow
Version:        svn19640.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(keyval.sty)
Provides:       tex(logreq.def) = %{tl_version}, tex(logreq.sty) = %{tl_version}

%description -n texlive-logreq
The package helps to automate a typical LaTeX workflow that
involves running LaTeX several times, running tools such as
BibTeX or makeindex, and so on. It will log requests like
"please rerun LaTeX" or "please run BibTeX on file X" to an
external XML file which lists all open tasks in a machine-
readable format. Compiler scripts and integrated LaTeX editing
environments may parse this file to determine the next steps in
the workflow in a way that is more efficient than parsing the
main log file. In sum, the package will do two things: enable
package authors to use LaTeX commands to issue requests,
collect all requests from all packages and write them to an
external XML file at the end of the document.

%package -n texlive-logreq-doc
Summary:        Documentation for logreq
Version:        svn19640.1.0

Provides:       tex-logreq-doc
AutoReqProv:    No

%description -n texlive-logreq-doc
Documentation for logreq

%package -n texlive-lm
Provides:       tex-lm = %{tl_version}
License:        GFSL
Summary:        Latin modern fonts in outline formats
Version:        svn48145
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(lm-cs.enc) = %{tl_version}, tex(lm-cssc.enc) = %{tl_version}
Provides:       tex(lm-cstt.enc) = %{tl_version}, tex(lm-ec.enc) = %{tl_version}
Provides:       tex(lm-l7x.enc) = %{tl_version}, tex(lm-mathex.enc) = %{tl_version}
Provides:       tex(lm-mathit.enc) = %{tl_version}, tex(lm-mathsy.enc) = %{tl_version}
Provides:       tex(lm-qx.enc) = %{tl_version}, tex(lm-qxsc.enc) = %{tl_version}
Provides:       tex(lm-qxtt.enc) = %{tl_version}, tex(lm-rep-cmin.enc) = %{tl_version}
Provides:       tex(lm-rep-cmit.enc) = %{tl_version}, tex(lm-rep-cmitt.enc) = %{tl_version}
Provides:       tex(lm-rep-cmrm.enc) = %{tl_version}, tex(lm-rep-cmsc.enc) = %{tl_version}
Provides:       tex(lm-rep-cmtt.enc) = %{tl_version}, tex(lm-rep-csin.enc) = %{tl_version}
Provides:       tex(lm-rep-csrm.enc) = %{tl_version}, tex(lm-rep-cssc.enc) = %{tl_version}
Provides:       tex(lm-rep-cstt.enc) = %{tl_version}, tex(lm-rep-plin.enc) = %{tl_version}
Provides:       tex(lm-rep-plit.enc) = %{tl_version}, tex(lm-rep-plitt.enc) = %{tl_version}
Provides:       tex(lm-rep-plrm.enc) = %{tl_version}, tex(lm-rep-plsc.enc) = %{tl_version}
Provides:       tex(lm-rep-pltt.enc) = %{tl_version}, tex(lm-rep-t5psn.enc) = %{tl_version}
Provides:       tex(lm-rm.enc) = %{tl_version}, tex(lm-rmsc.enc) = %{tl_version}
Provides:       tex(lm-rmtt.enc) = %{tl_version}, tex(lm-t5.enc) = %{tl_version}
Provides:       tex(lm-texnansi.enc) = %{tl_version}, tex(lm-ts1.enc) = %{tl_version}
Provides:       tex(lm-ec.map) = %{tl_version}, tex(lm-math.map) = %{tl_version}
Provides:       tex(lm-rm.map) = %{tl_version}, tex(lm-texnansi.map) = %{tl_version}
Provides:       tex(lm-cs.map) = %{tl_version}, tex(lm-ec.map) = %{tl_version}
Provides:       tex(lm-l7x.map) = %{tl_version}, tex(lm-math.map) = %{tl_version}
Provides:       tex(lm-qx.map) = %{tl_version}, tex(lm-rep-cmother.map) = %{tl_version}
Provides:       tex(lm-rep-cmtext-interpolated.map) = %{tl_version}
Provides:       tex(lm-rep-cmtext.map) = %{tl_version}, tex(lm-rep-cstext.map) = %{tl_version}
Provides:       tex(lm-rep-pltext.map) = %{tl_version}, tex(lm-rep-vntext.map) = %{tl_version}
Provides:       tex(lm-rm.map) = %{tl_version}, tex(lm-t5.map) = %{tl_version}
Provides:       tex(lm-texnansi.map) = %{tl_version}, tex(lm-ts1.map) = %{tl_version}
Provides:       tex(lm.map) = %{tl_version}, tex(lmmono10-italic.otf) = %{tl_version}
Provides:       tex(lmmono10-regular.otf) = %{tl_version}
Provides:       tex(lmmono12-regular.otf) = %{tl_version}
Provides:       tex(lmmono8-regular.otf) = %{tl_version}
Provides:       tex(lmmono9-regular.otf) = %{tl_version}
Provides:       tex(lmmonocaps10-oblique.otf) = %{tl_version}
Provides:       tex(lmmonocaps10-regular.otf) = %{tl_version}
Provides:       tex(lmmonolt10-bold.otf) = %{tl_version}
Provides:       tex(lmmonolt10-boldoblique.otf) = %{tl_version}
Provides:       tex(lmmonolt10-oblique.otf) = %{tl_version}
Provides:       tex(lmmonolt10-regular.otf) = %{tl_version}
Provides:       tex(lmmonoltcond10-oblique.otf) = %{tl_version}
Provides:       tex(lmmonoltcond10-regular.otf) = %{tl_version}
Provides:       tex(lmmonoprop10-oblique.otf) = %{tl_version}
Provides:       tex(lmmonoprop10-regular.otf) = %{tl_version}
Provides:       tex(lmmonoproplt10-bold.otf) = %{tl_version}
Provides:       tex(lmmonoproplt10-boldoblique.otf) = %{tl_version}
Provides:       tex(lmmonoproplt10-oblique.otf) = %{tl_version}
Provides:       tex(lmmonoproplt10-regular.otf) = %{tl_version}
Provides:       tex(lmmonoslant10-regular.otf) = %{tl_version}
Provides:       tex(lmroman10-bold.otf) = %{tl_version}, tex(lmroman10-bolditalic.otf) = %{tl_version}
Provides:       tex(lmroman10-italic.otf) = %{tl_version}
Provides:       tex(lmroman10-regular.otf) = %{tl_version}
Provides:       tex(lmroman12-bold.otf) = %{tl_version}, tex(lmroman12-italic.otf) = %{tl_version}
Provides:       tex(lmroman12-regular.otf) = %{tl_version}
Provides:       tex(lmroman17-regular.otf) = %{tl_version}
Provides:       tex(lmroman5-bold.otf) = %{tl_version}, tex(lmroman5-regular.otf) = %{tl_version}
Provides:       tex(lmroman6-bold.otf) = %{tl_version}, tex(lmroman6-regular.otf) = %{tl_version}
Provides:       tex(lmroman7-bold.otf) = %{tl_version}, tex(lmroman7-italic.otf) = %{tl_version}
Provides:       tex(lmroman7-regular.otf) = %{tl_version}
Provides:       tex(lmroman8-bold.otf) = %{tl_version}, tex(lmroman8-italic.otf) = %{tl_version}
Provides:       tex(lmroman8-regular.otf) = %{tl_version}
Provides:       tex(lmroman9-bold.otf) = %{tl_version}, tex(lmroman9-italic.otf) = %{tl_version}
Provides:       tex(lmroman9-regular.otf) = %{tl_version}
Provides:       tex(lmromancaps10-oblique.otf) = %{tl_version}
Provides:       tex(lmromancaps10-regular.otf) = %{tl_version}
Provides:       tex(lmromandemi10-oblique.otf) = %{tl_version}
Provides:       tex(lmromandemi10-regular.otf) = %{tl_version}
Provides:       tex(lmromandunh10-oblique.otf) = %{tl_version}
Provides:       tex(lmromandunh10-regular.otf) = %{tl_version}
Provides:       tex(lmromanslant10-bold.otf) = %{tl_version}
Provides:       tex(lmromanslant10-regular.otf) = %{tl_version}
Provides:       tex(lmromanslant12-regular.otf) = %{tl_version}
Provides:       tex(lmromanslant17-regular.otf) = %{tl_version}
Provides:       tex(lmromanslant8-regular.otf) = %{tl_version}
Provides:       tex(lmromanslant9-regular.otf) = %{tl_version}
Provides:       tex(lmromanunsl10-regular.otf) = %{tl_version}
Provides:       tex(lmsans10-bold.otf) = %{tl_version}, tex(lmsans10-boldoblique.otf) = %{tl_version}
Provides:       tex(lmsans10-oblique.otf) = %{tl_version}
Provides:       tex(lmsans10-regular.otf) = %{tl_version}
Provides:       tex(lmsans12-oblique.otf) = %{tl_version}
Provides:       tex(lmsans12-regular.otf) = %{tl_version}
Provides:       tex(lmsans17-oblique.otf) = %{tl_version}
Provides:       tex(lmsans17-regular.otf) = %{tl_version}
Provides:       tex(lmsans8-oblique.otf) = %{tl_version}
Provides:       tex(lmsans8-regular.otf) = %{tl_version}
Provides:       tex(lmsans9-oblique.otf) = %{tl_version}
Provides:       tex(lmsans9-regular.otf) = %{tl_version}
Provides:       tex(lmsansdemicond10-oblique.otf) = %{tl_version}
Provides:       tex(lmsansdemicond10-regular.otf) = %{tl_version}
Provides:       tex(lmsansquot8-bold.otf) = %{tl_version}
Provides:       tex(lmsansquot8-boldoblique.otf) = %{tl_version}
Provides:       tex(lmsansquot8-oblique.otf) = %{tl_version}
Provides:       tex(lmsansquot8-regular.otf) = %{tl_version}
Provides:       tex(cs-lmb10.tfm) = %{tl_version}, tex(cs-lmbo10.tfm) = %{tl_version}
Provides:       tex(cs-lmbx10.tfm) = %{tl_version}, tex(cs-lmbx12.tfm) = %{tl_version}
Provides:       tex(cs-lmbx5.tfm) = %{tl_version}, tex(cs-lmbx6.tfm) = %{tl_version}
Provides:       tex(cs-lmbx7.tfm) = %{tl_version}, tex(cs-lmbx8.tfm) = %{tl_version}
Provides:       tex(cs-lmbx9.tfm) = %{tl_version}, tex(cs-lmbxi10.tfm) = %{tl_version}
Provides:       tex(cs-lmbxo10.tfm) = %{tl_version}, tex(cs-lmcsc10.tfm) = %{tl_version}
Provides:       tex(cs-lmcsco10.tfm) = %{tl_version}, tex(cs-lmdunh10.tfm) = %{tl_version}
Provides:       tex(cs-lmduno10.tfm) = %{tl_version}, tex(cs-lmr10.tfm) = %{tl_version}
Provides:       tex(cs-lmr12.tfm) = %{tl_version}, tex(cs-lmr17.tfm) = %{tl_version}
Provides:       tex(cs-lmr5.tfm) = %{tl_version}, tex(cs-lmr6.tfm) = %{tl_version}
Provides:       tex(cs-lmr7.tfm) = %{tl_version}, tex(cs-lmr8.tfm) = %{tl_version}
Provides:       tex(cs-lmr9.tfm) = %{tl_version}, tex(cs-lmri10.tfm) = %{tl_version}
Provides:       tex(cs-lmri12.tfm) = %{tl_version}, tex(cs-lmri7.tfm) = %{tl_version}
Provides:       tex(cs-lmri8.tfm) = %{tl_version}, tex(cs-lmri9.tfm) = %{tl_version}
Provides:       tex(cs-lmro10.tfm) = %{tl_version}, tex(cs-lmro12.tfm) = %{tl_version}
Provides:       tex(cs-lmro17.tfm) = %{tl_version}, tex(cs-lmro8.tfm) = %{tl_version}
Provides:       tex(cs-lmro9.tfm) = %{tl_version}, tex(cs-lmss10.tfm) = %{tl_version}
Provides:       tex(cs-lmss12.tfm) = %{tl_version}, tex(cs-lmss17.tfm) = %{tl_version}
Provides:       tex(cs-lmss8.tfm) = %{tl_version}, tex(cs-lmss9.tfm) = %{tl_version}
Provides:       tex(cs-lmssbo10.tfm) = %{tl_version}, tex(cs-lmssbx10.tfm) = %{tl_version}
Provides:       tex(cs-lmssdc10.tfm) = %{tl_version}, tex(cs-lmssdo10.tfm) = %{tl_version}
Provides:       tex(cs-lmsso10.tfm) = %{tl_version}, tex(cs-lmsso12.tfm) = %{tl_version}
Provides:       tex(cs-lmsso17.tfm) = %{tl_version}, tex(cs-lmsso8.tfm) = %{tl_version}
Provides:       tex(cs-lmsso9.tfm) = %{tl_version}, tex(cs-lmssq8.tfm) = %{tl_version}
Provides:       tex(cs-lmssqbo8.tfm) = %{tl_version}, tex(cs-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(cs-lmssqo8.tfm) = %{tl_version}, tex(cs-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(cs-lmtcso10.tfm) = %{tl_version}, tex(cs-lmtk10.tfm) = %{tl_version}
Provides:       tex(cs-lmtko10.tfm) = %{tl_version}, tex(cs-lmtl10.tfm) = %{tl_version}
Provides:       tex(cs-lmtlc10.tfm) = %{tl_version}, tex(cs-lmtlco10.tfm) = %{tl_version}
Provides:       tex(cs-lmtlo10.tfm) = %{tl_version}, tex(cs-lmtt10.tfm) = %{tl_version}
Provides:       tex(cs-lmtt12.tfm) = %{tl_version}, tex(cs-lmtt8.tfm) = %{tl_version}
Provides:       tex(cs-lmtt9.tfm) = %{tl_version}, tex(cs-lmtti10.tfm) = %{tl_version}
Provides:       tex(cs-lmtto10.tfm) = %{tl_version}, tex(cs-lmu10.tfm) = %{tl_version}
Provides:       tex(cs-lmvtk10.tfm) = %{tl_version}, tex(cs-lmvtko10.tfm) = %{tl_version}
Provides:       tex(cs-lmvtl10.tfm) = %{tl_version}, tex(cs-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(cs-lmvtt10.tfm) = %{tl_version}, tex(cs-lmvtto10.tfm) = %{tl_version}
Provides:       tex(ec-lmb10.tfm) = %{tl_version}, tex(ec-lmbo10.tfm) = %{tl_version}
Provides:       tex(ec-lmbx10.tfm) = %{tl_version}, tex(ec-lmbx12.tfm) = %{tl_version}
Provides:       tex(ec-lmbx5.tfm) = %{tl_version}, tex(ec-lmbx6.tfm) = %{tl_version}
Provides:       tex(ec-lmbx7.tfm) = %{tl_version}, tex(ec-lmbx8.tfm) = %{tl_version}
Provides:       tex(ec-lmbx9.tfm) = %{tl_version}, tex(ec-lmbxi10.tfm) = %{tl_version}
Provides:       tex(ec-lmbxo10.tfm) = %{tl_version}, tex(ec-lmcsc10.tfm) = %{tl_version}
Provides:       tex(ec-lmcsco10.tfm) = %{tl_version}, tex(ec-lmdunh10.tfm) = %{tl_version}
Provides:       tex(ec-lmduno10.tfm) = %{tl_version}, tex(ec-lmr10.tfm) = %{tl_version}
Provides:       tex(ec-lmr12.tfm) = %{tl_version}, tex(ec-lmr17.tfm) = %{tl_version}
Provides:       tex(ec-lmr5.tfm) = %{tl_version}, tex(ec-lmr6.tfm) = %{tl_version}
Provides:       tex(ec-lmr7.tfm) = %{tl_version}, tex(ec-lmr8.tfm) = %{tl_version}
Provides:       tex(ec-lmr9.tfm) = %{tl_version}, tex(ec-lmri10.tfm) = %{tl_version}
Provides:       tex(ec-lmri12.tfm) = %{tl_version}, tex(ec-lmri7.tfm) = %{tl_version}
Provides:       tex(ec-lmri8.tfm) = %{tl_version}, tex(ec-lmri9.tfm) = %{tl_version}
Provides:       tex(ec-lmro10.tfm) = %{tl_version}, tex(ec-lmro12.tfm) = %{tl_version}
Provides:       tex(ec-lmro17.tfm) = %{tl_version}, tex(ec-lmro8.tfm) = %{tl_version}
Provides:       tex(ec-lmro9.tfm) = %{tl_version}, tex(ec-lmss10.tfm) = %{tl_version}
Provides:       tex(ec-lmss12.tfm) = %{tl_version}, tex(ec-lmss17.tfm) = %{tl_version}
Provides:       tex(ec-lmss8.tfm) = %{tl_version}, tex(ec-lmss9.tfm) = %{tl_version}
Provides:       tex(ec-lmssbo10.tfm) = %{tl_version}, tex(ec-lmssbx10.tfm) = %{tl_version}
Provides:       tex(ec-lmssdc10.tfm) = %{tl_version}, tex(ec-lmssdo10.tfm) = %{tl_version}
Provides:       tex(ec-lmsso10.tfm) = %{tl_version}, tex(ec-lmsso12.tfm) = %{tl_version}
Provides:       tex(ec-lmsso17.tfm) = %{tl_version}, tex(ec-lmsso8.tfm) = %{tl_version}
Provides:       tex(ec-lmsso9.tfm) = %{tl_version}, tex(ec-lmssq8.tfm) = %{tl_version}
Provides:       tex(ec-lmssqbo8.tfm) = %{tl_version}, tex(ec-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(ec-lmssqo8.tfm) = %{tl_version}, tex(ec-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(ec-lmtcso10.tfm) = %{tl_version}, tex(ec-lmtk10.tfm) = %{tl_version}
Provides:       tex(ec-lmtko10.tfm) = %{tl_version}, tex(ec-lmtl10.tfm) = %{tl_version}
Provides:       tex(ec-lmtlc10.tfm) = %{tl_version}, tex(ec-lmtlco10.tfm) = %{tl_version}
Provides:       tex(ec-lmtlo10.tfm) = %{tl_version}, tex(ec-lmtt10.tfm) = %{tl_version}
Provides:       tex(ec-lmtt12.tfm) = %{tl_version}, tex(ec-lmtt8.tfm) = %{tl_version}
Provides:       tex(ec-lmtt9.tfm) = %{tl_version}, tex(ec-lmtti10.tfm) = %{tl_version}
Provides:       tex(ec-lmtto10.tfm) = %{tl_version}, tex(ec-lmu10.tfm) = %{tl_version}
Provides:       tex(ec-lmvtk10.tfm) = %{tl_version}, tex(ec-lmvtko10.tfm) = %{tl_version}
Provides:       tex(ec-lmvtl10.tfm) = %{tl_version}, tex(ec-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(ec-lmvtt10.tfm) = %{tl_version}, tex(ec-lmvtto10.tfm) = %{tl_version}
Provides:       tex(l7x-lmb10.tfm) = %{tl_version}, tex(l7x-lmbo10.tfm) = %{tl_version}
Provides:       tex(l7x-lmbx10.tfm) = %{tl_version}, tex(l7x-lmbx12.tfm) = %{tl_version}
Provides:       tex(l7x-lmbx5.tfm) = %{tl_version}, tex(l7x-lmbx6.tfm) = %{tl_version}
Provides:       tex(l7x-lmbx7.tfm) = %{tl_version}, tex(l7x-lmbx8.tfm) = %{tl_version}
Provides:       tex(l7x-lmbx9.tfm) = %{tl_version}, tex(l7x-lmbxi10.tfm) = %{tl_version}
Provides:       tex(l7x-lmbxo10.tfm) = %{tl_version}, tex(l7x-lmcsc10.tfm) = %{tl_version}
Provides:       tex(l7x-lmcsco10.tfm) = %{tl_version}, tex(l7x-lmdunh10.tfm) = %{tl_version}
Provides:       tex(l7x-lmduno10.tfm) = %{tl_version}, tex(l7x-lmr10.tfm) = %{tl_version}
Provides:       tex(l7x-lmr12.tfm) = %{tl_version}, tex(l7x-lmr17.tfm) = %{tl_version}
Provides:       tex(l7x-lmr5.tfm) = %{tl_version}, tex(l7x-lmr6.tfm) = %{tl_version}
Provides:       tex(l7x-lmr7.tfm) = %{tl_version}, tex(l7x-lmr8.tfm) = %{tl_version}
Provides:       tex(l7x-lmr9.tfm) = %{tl_version}, tex(l7x-lmri10.tfm) = %{tl_version}
Provides:       tex(l7x-lmri12.tfm) = %{tl_version}, tex(l7x-lmri7.tfm) = %{tl_version}
Provides:       tex(l7x-lmri8.tfm) = %{tl_version}, tex(l7x-lmri9.tfm) = %{tl_version}
Provides:       tex(l7x-lmro10.tfm) = %{tl_version}, tex(l7x-lmro12.tfm) = %{tl_version}
Provides:       tex(l7x-lmro17.tfm) = %{tl_version}, tex(l7x-lmro8.tfm) = %{tl_version}
Provides:       tex(l7x-lmro9.tfm) = %{tl_version}, tex(l7x-lmss10.tfm) = %{tl_version}
Provides:       tex(l7x-lmss12.tfm) = %{tl_version}, tex(l7x-lmss17.tfm) = %{tl_version}
Provides:       tex(l7x-lmss8.tfm) = %{tl_version}, tex(l7x-lmss9.tfm) = %{tl_version}
Provides:       tex(l7x-lmssbo10.tfm) = %{tl_version}, tex(l7x-lmssbx10.tfm) = %{tl_version}
Provides:       tex(l7x-lmssdc10.tfm) = %{tl_version}, tex(l7x-lmssdo10.tfm) = %{tl_version}
Provides:       tex(l7x-lmsso10.tfm) = %{tl_version}, tex(l7x-lmsso12.tfm) = %{tl_version}
Provides:       tex(l7x-lmsso17.tfm) = %{tl_version}, tex(l7x-lmsso8.tfm) = %{tl_version}
Provides:       tex(l7x-lmsso9.tfm) = %{tl_version}, tex(l7x-lmssq8.tfm) = %{tl_version}
Provides:       tex(l7x-lmssqbo8.tfm) = %{tl_version}, tex(l7x-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(l7x-lmssqo8.tfm) = %{tl_version}, tex(l7x-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtcso10.tfm) = %{tl_version}, tex(l7x-lmtk10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtko10.tfm) = %{tl_version}, tex(l7x-lmtl10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtlc10.tfm) = %{tl_version}, tex(l7x-lmtlco10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtlo10.tfm) = %{tl_version}, tex(l7x-lmtt10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtt12.tfm) = %{tl_version}, tex(l7x-lmtt8.tfm) = %{tl_version}
Provides:       tex(l7x-lmtt9.tfm) = %{tl_version}, tex(l7x-lmtti10.tfm) = %{tl_version}
Provides:       tex(l7x-lmtto10.tfm) = %{tl_version}, tex(l7x-lmu10.tfm) = %{tl_version}
Provides:       tex(l7x-lmvtk10.tfm) = %{tl_version}, tex(l7x-lmvtko10.tfm) = %{tl_version}
Provides:       tex(l7x-lmvtl10.tfm) = %{tl_version}, tex(l7x-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(l7x-lmvtt10.tfm) = %{tl_version}, tex(l7x-lmvtto10.tfm) = %{tl_version}
Provides:       tex(lmbsy10.tfm) = %{tl_version}, tex(lmbsy5.tfm) = %{tl_version}
Provides:       tex(lmbsy7.tfm) = %{tl_version}, tex(lmex10.tfm) = %{tl_version}
Provides:       tex(lmmi10.tfm) = %{tl_version}, tex(lmmi12.tfm) = %{tl_version}
Provides:       tex(lmmi5.tfm) = %{tl_version}, tex(lmmi6.tfm) = %{tl_version}
Provides:       tex(lmmi7.tfm) = %{tl_version}, tex(lmmi8.tfm) = %{tl_version}
Provides:       tex(lmmi9.tfm) = %{tl_version}, tex(lmmib10.tfm) = %{tl_version}
Provides:       tex(lmmib5.tfm) = %{tl_version}, tex(lmmib7.tfm) = %{tl_version}
Provides:       tex(lmsy10.tfm) = %{tl_version}, tex(lmsy5.tfm) = %{tl_version}
Provides:       tex(lmsy6.tfm) = %{tl_version}, tex(lmsy7.tfm) = %{tl_version}
Provides:       tex(lmsy8.tfm) = %{tl_version}, tex(lmsy9.tfm) = %{tl_version}
Provides:       tex(qx-lmb10.tfm) = %{tl_version}, tex(qx-lmbo10.tfm) = %{tl_version}
Provides:       tex(qx-lmbx10.tfm) = %{tl_version}, tex(qx-lmbx12.tfm) = %{tl_version}
Provides:       tex(qx-lmbx5.tfm) = %{tl_version}, tex(qx-lmbx6.tfm) = %{tl_version}
Provides:       tex(qx-lmbx7.tfm) = %{tl_version}, tex(qx-lmbx8.tfm) = %{tl_version}
Provides:       tex(qx-lmbx9.tfm) = %{tl_version}, tex(qx-lmbxi10.tfm) = %{tl_version}
Provides:       tex(qx-lmbxo10.tfm) = %{tl_version}, tex(qx-lmcsc10.tfm) = %{tl_version}
Provides:       tex(qx-lmcsco10.tfm) = %{tl_version}, tex(qx-lmdunh10.tfm) = %{tl_version}
Provides:       tex(qx-lmduno10.tfm) = %{tl_version}, tex(qx-lmr10.tfm) = %{tl_version}
Provides:       tex(qx-lmr12.tfm) = %{tl_version}, tex(qx-lmr17.tfm) = %{tl_version}
Provides:       tex(qx-lmr5.tfm) = %{tl_version}, tex(qx-lmr6.tfm) = %{tl_version}
Provides:       tex(qx-lmr7.tfm) = %{tl_version}, tex(qx-lmr8.tfm) = %{tl_version}
Provides:       tex(qx-lmr9.tfm) = %{tl_version}, tex(qx-lmri10.tfm) = %{tl_version}
Provides:       tex(qx-lmri12.tfm) = %{tl_version}, tex(qx-lmri7.tfm) = %{tl_version}
Provides:       tex(qx-lmri8.tfm) = %{tl_version}, tex(qx-lmri9.tfm) = %{tl_version}
Provides:       tex(qx-lmro10.tfm) = %{tl_version}, tex(qx-lmro12.tfm) = %{tl_version}
Provides:       tex(qx-lmro17.tfm) = %{tl_version}, tex(qx-lmro8.tfm) = %{tl_version}
Provides:       tex(qx-lmro9.tfm) = %{tl_version}, tex(qx-lmss10.tfm) = %{tl_version}
Provides:       tex(qx-lmss12.tfm) = %{tl_version}, tex(qx-lmss17.tfm) = %{tl_version}
Provides:       tex(qx-lmss8.tfm) = %{tl_version}, tex(qx-lmss9.tfm) = %{tl_version}
Provides:       tex(qx-lmssbo10.tfm) = %{tl_version}, tex(qx-lmssbx10.tfm) = %{tl_version}
Provides:       tex(qx-lmssdc10.tfm) = %{tl_version}, tex(qx-lmssdo10.tfm) = %{tl_version}
Provides:       tex(qx-lmsso10.tfm) = %{tl_version}, tex(qx-lmsso12.tfm) = %{tl_version}
Provides:       tex(qx-lmsso17.tfm) = %{tl_version}, tex(qx-lmsso8.tfm) = %{tl_version}
Provides:       tex(qx-lmsso9.tfm) = %{tl_version}, tex(qx-lmssq8.tfm) = %{tl_version}
Provides:       tex(qx-lmssqbo8.tfm) = %{tl_version}, tex(qx-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(qx-lmssqo8.tfm) = %{tl_version}, tex(qx-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(qx-lmtcso10.tfm) = %{tl_version}, tex(qx-lmtk10.tfm) = %{tl_version}
Provides:       tex(qx-lmtko10.tfm) = %{tl_version}, tex(qx-lmtl10.tfm) = %{tl_version}
Provides:       tex(qx-lmtlc10.tfm) = %{tl_version}, tex(qx-lmtlco10.tfm) = %{tl_version}
Provides:       tex(qx-lmtlo10.tfm) = %{tl_version}, tex(qx-lmtt10.tfm) = %{tl_version}
Provides:       tex(qx-lmtt12.tfm) = %{tl_version}, tex(qx-lmtt8.tfm) = %{tl_version}
Provides:       tex(qx-lmtt9.tfm) = %{tl_version}, tex(qx-lmtti10.tfm) = %{tl_version}
Provides:       tex(qx-lmtto10.tfm) = %{tl_version}, tex(qx-lmu10.tfm) = %{tl_version}
Provides:       tex(qx-lmvtk10.tfm) = %{tl_version}, tex(qx-lmvtko10.tfm) = %{tl_version}
Provides:       tex(qx-lmvtl10.tfm) = %{tl_version}, tex(qx-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(qx-lmvtt10.tfm) = %{tl_version}, tex(qx-lmvtto10.tfm) = %{tl_version}
Provides:       tex(rm-lmb10.tfm) = %{tl_version}, tex(rm-lmbo10.tfm) = %{tl_version}
Provides:       tex(rm-lmbx10.tfm) = %{tl_version}, tex(rm-lmbx12.tfm) = %{tl_version}
Provides:       tex(rm-lmbx5.tfm) = %{tl_version}, tex(rm-lmbx6.tfm) = %{tl_version}
Provides:       tex(rm-lmbx7.tfm) = %{tl_version}, tex(rm-lmbx8.tfm) = %{tl_version}
Provides:       tex(rm-lmbx9.tfm) = %{tl_version}, tex(rm-lmbxi10.tfm) = %{tl_version}
Provides:       tex(rm-lmbxo10.tfm) = %{tl_version}, tex(rm-lmcsc10.tfm) = %{tl_version}
Provides:       tex(rm-lmcsco10.tfm) = %{tl_version}, tex(rm-lmdunh10.tfm) = %{tl_version}
Provides:       tex(rm-lmduno10.tfm) = %{tl_version}, tex(rm-lmr10.tfm) = %{tl_version}
Provides:       tex(rm-lmr12.tfm) = %{tl_version}, tex(rm-lmr17.tfm) = %{tl_version}
Provides:       tex(rm-lmr5.tfm) = %{tl_version}, tex(rm-lmr6.tfm) = %{tl_version}
Provides:       tex(rm-lmr7.tfm) = %{tl_version}, tex(rm-lmr8.tfm) = %{tl_version}
Provides:       tex(rm-lmr9.tfm) = %{tl_version}, tex(rm-lmri10.tfm) = %{tl_version}
Provides:       tex(rm-lmri12.tfm) = %{tl_version}, tex(rm-lmri7.tfm) = %{tl_version}
Provides:       tex(rm-lmri8.tfm) = %{tl_version}, tex(rm-lmri9.tfm) = %{tl_version}
Provides:       tex(rm-lmro10.tfm) = %{tl_version}, tex(rm-lmro12.tfm) = %{tl_version}
Provides:       tex(rm-lmro17.tfm) = %{tl_version}, tex(rm-lmro8.tfm) = %{tl_version}
Provides:       tex(rm-lmro9.tfm) = %{tl_version}, tex(rm-lmss10.tfm) = %{tl_version}
Provides:       tex(rm-lmss12.tfm) = %{tl_version}, tex(rm-lmss17.tfm) = %{tl_version}
Provides:       tex(rm-lmss8.tfm) = %{tl_version}, tex(rm-lmss9.tfm) = %{tl_version}
Provides:       tex(rm-lmssbo10.tfm) = %{tl_version}, tex(rm-lmssbx10.tfm) = %{tl_version}
Provides:       tex(rm-lmssdc10.tfm) = %{tl_version}, tex(rm-lmssdo10.tfm) = %{tl_version}
Provides:       tex(rm-lmsso10.tfm) = %{tl_version}, tex(rm-lmsso12.tfm) = %{tl_version}
Provides:       tex(rm-lmsso17.tfm) = %{tl_version}, tex(rm-lmsso8.tfm) = %{tl_version}
Provides:       tex(rm-lmsso9.tfm) = %{tl_version}, tex(rm-lmssq8.tfm) = %{tl_version}
Provides:       tex(rm-lmssqbo8.tfm) = %{tl_version}, tex(rm-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(rm-lmssqo8.tfm) = %{tl_version}, tex(rm-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(rm-lmtcso10.tfm) = %{tl_version}, tex(rm-lmtk10.tfm) = %{tl_version}
Provides:       tex(rm-lmtko10.tfm) = %{tl_version}, tex(rm-lmtl10.tfm) = %{tl_version}
Provides:       tex(rm-lmtlc10.tfm) = %{tl_version}, tex(rm-lmtlco10.tfm) = %{tl_version}
Provides:       tex(rm-lmtlo10.tfm) = %{tl_version}, tex(rm-lmtt10.tfm) = %{tl_version}
Provides:       tex(rm-lmtt12.tfm) = %{tl_version}, tex(rm-lmtt8.tfm) = %{tl_version}
Provides:       tex(rm-lmtt9.tfm) = %{tl_version}, tex(rm-lmtti10.tfm) = %{tl_version}
Provides:       tex(rm-lmtto10.tfm) = %{tl_version}, tex(rm-lmu10.tfm) = %{tl_version}
Provides:       tex(rm-lmvtk10.tfm) = %{tl_version}, tex(rm-lmvtko10.tfm) = %{tl_version}
Provides:       tex(rm-lmvtl10.tfm) = %{tl_version}, tex(rm-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(rm-lmvtt10.tfm) = %{tl_version}, tex(rm-lmvtto10.tfm) = %{tl_version}
Provides:       tex(t5-lmb10.tfm) = %{tl_version}, tex(t5-lmbo10.tfm) = %{tl_version}
Provides:       tex(t5-lmbx10.tfm) = %{tl_version}, tex(t5-lmbx12.tfm) = %{tl_version}
Provides:       tex(t5-lmbx5.tfm) = %{tl_version}, tex(t5-lmbx6.tfm) = %{tl_version}
Provides:       tex(t5-lmbx7.tfm) = %{tl_version}, tex(t5-lmbx8.tfm) = %{tl_version}
Provides:       tex(t5-lmbx9.tfm) = %{tl_version}, tex(t5-lmbxi10.tfm) = %{tl_version}
Provides:       tex(t5-lmbxo10.tfm) = %{tl_version}, tex(t5-lmcsc10.tfm) = %{tl_version}
Provides:       tex(t5-lmcsco10.tfm) = %{tl_version}, tex(t5-lmdunh10.tfm) = %{tl_version}
Provides:       tex(t5-lmduno10.tfm) = %{tl_version}, tex(t5-lmr10.tfm) = %{tl_version}
Provides:       tex(t5-lmr12.tfm) = %{tl_version}, tex(t5-lmr17.tfm) = %{tl_version}
Provides:       tex(t5-lmr5.tfm) = %{tl_version}, tex(t5-lmr6.tfm) = %{tl_version}
Provides:       tex(t5-lmr7.tfm) = %{tl_version}, tex(t5-lmr8.tfm) = %{tl_version}
Provides:       tex(t5-lmr9.tfm) = %{tl_version}, tex(t5-lmri10.tfm) = %{tl_version}
Provides:       tex(t5-lmri12.tfm) = %{tl_version}, tex(t5-lmri7.tfm) = %{tl_version}
Provides:       tex(t5-lmri8.tfm) = %{tl_version}, tex(t5-lmri9.tfm) = %{tl_version}
Provides:       tex(t5-lmro10.tfm) = %{tl_version}, tex(t5-lmro12.tfm) = %{tl_version}
Provides:       tex(t5-lmro17.tfm) = %{tl_version}, tex(t5-lmro8.tfm) = %{tl_version}
Provides:       tex(t5-lmro9.tfm) = %{tl_version}, tex(t5-lmss10.tfm) = %{tl_version}
Provides:       tex(t5-lmss12.tfm) = %{tl_version}, tex(t5-lmss17.tfm) = %{tl_version}
Provides:       tex(t5-lmss8.tfm) = %{tl_version}, tex(t5-lmss9.tfm) = %{tl_version}
Provides:       tex(t5-lmssbo10.tfm) = %{tl_version}, tex(t5-lmssbx10.tfm) = %{tl_version}
Provides:       tex(t5-lmssdc10.tfm) = %{tl_version}, tex(t5-lmssdo10.tfm) = %{tl_version}
Provides:       tex(t5-lmsso10.tfm) = %{tl_version}, tex(t5-lmsso12.tfm) = %{tl_version}
Provides:       tex(t5-lmsso17.tfm) = %{tl_version}, tex(t5-lmsso8.tfm) = %{tl_version}
Provides:       tex(t5-lmsso9.tfm) = %{tl_version}, tex(t5-lmssq8.tfm) = %{tl_version}
Provides:       tex(t5-lmssqbo8.tfm) = %{tl_version}, tex(t5-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(t5-lmssqo8.tfm) = %{tl_version}, tex(t5-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(t5-lmtcso10.tfm) = %{tl_version}, tex(t5-lmtk10.tfm) = %{tl_version}
Provides:       tex(t5-lmtko10.tfm) = %{tl_version}, tex(t5-lmtl10.tfm) = %{tl_version}
Provides:       tex(t5-lmtlc10.tfm) = %{tl_version}, tex(t5-lmtlco10.tfm) = %{tl_version}
Provides:       tex(t5-lmtlo10.tfm) = %{tl_version}, tex(t5-lmtt10.tfm) = %{tl_version}
Provides:       tex(t5-lmtt12.tfm) = %{tl_version}, tex(t5-lmtt8.tfm) = %{tl_version}
Provides:       tex(t5-lmtt9.tfm) = %{tl_version}, tex(t5-lmtti10.tfm) = %{tl_version}
Provides:       tex(t5-lmtto10.tfm) = %{tl_version}, tex(t5-lmu10.tfm) = %{tl_version}
Provides:       tex(t5-lmvtk10.tfm) = %{tl_version}, tex(t5-lmvtko10.tfm) = %{tl_version}
Provides:       tex(t5-lmvtl10.tfm) = %{tl_version}, tex(t5-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(t5-lmvtt10.tfm) = %{tl_version}, tex(t5-lmvtto10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmb10.tfm) = %{tl_version}, tex(texnansi-lmbo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbx10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbx12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbx5.tfm) = %{tl_version}, tex(texnansi-lmbx6.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbx7.tfm) = %{tl_version}, tex(texnansi-lmbx8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbx9.tfm) = %{tl_version}, tex(texnansi-lmbxi10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmbxo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmcsc10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmcsco10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmdunh10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmduno10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmr10.tfm) = %{tl_version}, tex(texnansi-lmr12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmr17.tfm) = %{tl_version}, tex(texnansi-lmr5.tfm) = %{tl_version}
Provides:       tex(texnansi-lmr6.tfm) = %{tl_version}, tex(texnansi-lmr7.tfm) = %{tl_version}
Provides:       tex(texnansi-lmr8.tfm) = %{tl_version}, tex(texnansi-lmr9.tfm) = %{tl_version}
Provides:       tex(texnansi-lmri10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmri12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmri7.tfm) = %{tl_version}, tex(texnansi-lmri8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmri9.tfm) = %{tl_version}, tex(texnansi-lmro10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmro12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmro17.tfm) = %{tl_version}
Provides:       tex(texnansi-lmro8.tfm) = %{tl_version}, tex(texnansi-lmro9.tfm) = %{tl_version}
Provides:       tex(texnansi-lmss10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmss12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmss17.tfm) = %{tl_version}
Provides:       tex(texnansi-lmss8.tfm) = %{tl_version}, tex(texnansi-lmss9.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssbo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssbx10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssdc10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssdo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmsso10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmsso12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmsso17.tfm) = %{tl_version}
Provides:       tex(texnansi-lmsso8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmsso9.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssq8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssqbo8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmssqo8.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtcso10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtk10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtko10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtl10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtlc10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtlco10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtlo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtt10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtt12.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtt8.tfm) = %{tl_version}, tex(texnansi-lmtt9.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtti10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmtto10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmu10.tfm) = %{tl_version}, tex(texnansi-lmvtk10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmvtko10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmvtl10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmvtt10.tfm) = %{tl_version}
Provides:       tex(texnansi-lmvtto10.tfm) = %{tl_version}
Provides:       tex(ts1-lmb10.tfm) = %{tl_version}, tex(ts1-lmbo10.tfm) = %{tl_version}
Provides:       tex(ts1-lmbx10.tfm) = %{tl_version}, tex(ts1-lmbx12.tfm) = %{tl_version}
Provides:       tex(ts1-lmbx5.tfm) = %{tl_version}, tex(ts1-lmbx6.tfm) = %{tl_version}
Provides:       tex(ts1-lmbx7.tfm) = %{tl_version}, tex(ts1-lmbx8.tfm) = %{tl_version}
Provides:       tex(ts1-lmbx9.tfm) = %{tl_version}, tex(ts1-lmbxi10.tfm) = %{tl_version}
Provides:       tex(ts1-lmbxo10.tfm) = %{tl_version}, tex(ts1-lmcsc10.tfm) = %{tl_version}
Provides:       tex(ts1-lmcsco10.tfm) = %{tl_version}, tex(ts1-lmdunh10.tfm) = %{tl_version}
Provides:       tex(ts1-lmduno10.tfm) = %{tl_version}, tex(ts1-lmr10.tfm) = %{tl_version}
Provides:       tex(ts1-lmr12.tfm) = %{tl_version}, tex(ts1-lmr17.tfm) = %{tl_version}
Provides:       tex(ts1-lmr5.tfm) = %{tl_version}, tex(ts1-lmr6.tfm) = %{tl_version}
Provides:       tex(ts1-lmr7.tfm) = %{tl_version}, tex(ts1-lmr8.tfm) = %{tl_version}
Provides:       tex(ts1-lmr9.tfm) = %{tl_version}, tex(ts1-lmri10.tfm) = %{tl_version}
Provides:       tex(ts1-lmri12.tfm) = %{tl_version}, tex(ts1-lmri7.tfm) = %{tl_version}
Provides:       tex(ts1-lmri8.tfm) = %{tl_version}, tex(ts1-lmri9.tfm) = %{tl_version}
Provides:       tex(ts1-lmro10.tfm) = %{tl_version}, tex(ts1-lmro12.tfm) = %{tl_version}
Provides:       tex(ts1-lmro17.tfm) = %{tl_version}, tex(ts1-lmro8.tfm) = %{tl_version}
Provides:       tex(ts1-lmro9.tfm) = %{tl_version}, tex(ts1-lmss10.tfm) = %{tl_version}
Provides:       tex(ts1-lmss12.tfm) = %{tl_version}, tex(ts1-lmss17.tfm) = %{tl_version}
Provides:       tex(ts1-lmss8.tfm) = %{tl_version}, tex(ts1-lmss9.tfm) = %{tl_version}
Provides:       tex(ts1-lmssbo10.tfm) = %{tl_version}, tex(ts1-lmssbx10.tfm) = %{tl_version}
Provides:       tex(ts1-lmssdc10.tfm) = %{tl_version}, tex(ts1-lmssdo10.tfm) = %{tl_version}
Provides:       tex(ts1-lmsso10.tfm) = %{tl_version}, tex(ts1-lmsso12.tfm) = %{tl_version}
Provides:       tex(ts1-lmsso17.tfm) = %{tl_version}, tex(ts1-lmsso8.tfm) = %{tl_version}
Provides:       tex(ts1-lmsso9.tfm) = %{tl_version}, tex(ts1-lmssq8.tfm) = %{tl_version}
Provides:       tex(ts1-lmssqbo8.tfm) = %{tl_version}, tex(ts1-lmssqbx8.tfm) = %{tl_version}
Provides:       tex(ts1-lmssqo8.tfm) = %{tl_version}, tex(ts1-lmtcsc10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtcso10.tfm) = %{tl_version}, tex(ts1-lmtk10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtko10.tfm) = %{tl_version}, tex(ts1-lmtl10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtlc10.tfm) = %{tl_version}, tex(ts1-lmtlco10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtlo10.tfm) = %{tl_version}, tex(ts1-lmtt10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtt12.tfm) = %{tl_version}, tex(ts1-lmtt8.tfm) = %{tl_version}
Provides:       tex(ts1-lmtt9.tfm) = %{tl_version}, tex(ts1-lmtti10.tfm) = %{tl_version}
Provides:       tex(ts1-lmtto10.tfm) = %{tl_version}, tex(ts1-lmu10.tfm) = %{tl_version}
Provides:       tex(ts1-lmvtk10.tfm) = %{tl_version}, tex(ts1-lmvtko10.tfm) = %{tl_version}
Provides:       tex(ts1-lmvtl10.tfm) = %{tl_version}, tex(ts1-lmvtlo10.tfm) = %{tl_version}
Provides:       tex(ts1-lmvtt10.tfm) = %{tl_version}, tex(ts1-lmvtto10.tfm) = %{tl_version}
Provides:       tex(lmb10.pfb) = %{tl_version}, tex(lmbo10.pfb) = %{tl_version}
Provides:       tex(lmbsy10.pfb) = %{tl_version}, tex(lmbsy5.pfb) = %{tl_version}
Provides:       tex(lmbsy7.pfb) = %{tl_version}, tex(lmbx10.pfb) = %{tl_version}
Provides:       tex(lmbx12.pfb) = %{tl_version}, tex(lmbx5.pfb) = %{tl_version}
Provides:       tex(lmbx6.pfb) = %{tl_version}, tex(lmbx7.pfb) = %{tl_version}
Provides:       tex(lmbx8.pfb) = %{tl_version}, tex(lmbx9.pfb) = %{tl_version}
Provides:       tex(lmbxi10.pfb) = %{tl_version}, tex(lmbxo10.pfb) = %{tl_version}
Provides:       tex(lmcsc10.pfb) = %{tl_version}, tex(lmcsco10.pfb) = %{tl_version}
Provides:       tex(lmdunh10.pfb) = %{tl_version}, tex(lmduno10.pfb) = %{tl_version}
Provides:       tex(lmex10.pfb) = %{tl_version}, tex(lmmi10.pfb) = %{tl_version}
Provides:       tex(lmmi12.pfb) = %{tl_version}, tex(lmmi5.pfb) = %{tl_version}
Provides:       tex(lmmi6.pfb) = %{tl_version}, tex(lmmi7.pfb) = %{tl_version}
Provides:       tex(lmmi8.pfb) = %{tl_version}, tex(lmmi9.pfb) = %{tl_version}
Provides:       tex(lmmib10.pfb) = %{tl_version}, tex(lmmib5.pfb) = %{tl_version}
Provides:       tex(lmmib7.pfb) = %{tl_version}, tex(lmr10.pfb) = %{tl_version}
Provides:       tex(lmr12.pfb) = %{tl_version}, tex(lmr17.pfb) = %{tl_version}
Provides:       tex(lmr5.pfb) = %{tl_version}, tex(lmr6.pfb) = %{tl_version}
Provides:       tex(lmr7.pfb) = %{tl_version}, tex(lmr8.pfb) = %{tl_version}
Provides:       tex(lmr9.pfb) = %{tl_version}, tex(lmri10.pfb) = %{tl_version}
Provides:       tex(lmri12.pfb) = %{tl_version}, tex(lmri7.pfb) = %{tl_version}
Provides:       tex(lmri8.pfb) = %{tl_version}, tex(lmri9.pfb) = %{tl_version}
Provides:       tex(lmro10.pfb) = %{tl_version}, tex(lmro12.pfb) = %{tl_version}
Provides:       tex(lmro17.pfb) = %{tl_version}, tex(lmro8.pfb) = %{tl_version}
Provides:       tex(lmro9.pfb) = %{tl_version}, tex(lmss10.pfb) = %{tl_version}
Provides:       tex(lmss12.pfb) = %{tl_version}, tex(lmss17.pfb) = %{tl_version}
Provides:       tex(lmss8.pfb) = %{tl_version}, tex(lmss9.pfb) = %{tl_version}
Provides:       tex(lmssbo10.pfb) = %{tl_version}, tex(lmssbx10.pfb) = %{tl_version}
Provides:       tex(lmssdc10.pfb) = %{tl_version}, tex(lmssdo10.pfb) = %{tl_version}
Provides:       tex(lmsso10.pfb) = %{tl_version}, tex(lmsso12.pfb) = %{tl_version}
Provides:       tex(lmsso17.pfb) = %{tl_version}, tex(lmsso8.pfb) = %{tl_version}
Provides:       tex(lmsso9.pfb) = %{tl_version}, tex(lmssq8.pfb) = %{tl_version}
Provides:       tex(lmssqbo8.pfb) = %{tl_version}, tex(lmssqbx8.pfb) = %{tl_version}
Provides:       tex(lmssqo8.pfb) = %{tl_version}, tex(lmsy10.pfb) = %{tl_version}
Provides:       tex(lmsy5.pfb) = %{tl_version}, tex(lmsy6.pfb) = %{tl_version}
Provides:       tex(lmsy7.pfb) = %{tl_version}, tex(lmsy8.pfb) = %{tl_version}
Provides:       tex(lmsy9.pfb) = %{tl_version}, tex(lmtcsc10.pfb) = %{tl_version}
Provides:       tex(lmtcso10.pfb) = %{tl_version}, tex(lmtk10.pfb) = %{tl_version}
Provides:       tex(lmtko10.pfb) = %{tl_version}, tex(lmtl10.pfb) = %{tl_version}
Provides:       tex(lmtlc10.pfb) = %{tl_version}, tex(lmtlco10.pfb) = %{tl_version}
Provides:       tex(lmtlo10.pfb) = %{tl_version}, tex(lmtt10.pfb) = %{tl_version}
Provides:       tex(lmtt12.pfb) = %{tl_version}, tex(lmtt8.pfb) = %{tl_version}
Provides:       tex(lmtt9.pfb) = %{tl_version}, tex(lmtti10.pfb) = %{tl_version}
Provides:       tex(lmtto10.pfb) = %{tl_version}, tex(lmu10.pfb) = %{tl_version}
Provides:       tex(lmvtk10.pfb) = %{tl_version}, tex(lmvtko10.pfb) = %{tl_version}
Provides:       tex(lmvtl10.pfb) = %{tl_version}, tex(lmvtlo10.pfb) = %{tl_version}
Provides:       tex(lmvtt10.pfb) = %{tl_version}, tex(lmvtto10.pfb) = %{tl_version}
Provides:       tex(il2lmdh.fd) = %{tl_version}, tex(il2lmr.fd) = %{tl_version}
Provides:       tex(il2lmss.fd) = %{tl_version}, tex(il2lmssq.fd) = %{tl_version}
Provides:       tex(il2lmtt.fd) = %{tl_version}, tex(il2lmvtt.fd) = %{tl_version}
Provides:       tex(l7xlmdh.fd) = %{tl_version}, tex(l7xlmr.fd) = %{tl_version}
Provides:       tex(l7xlmss.fd) = %{tl_version}, tex(l7xlmssq.fd) = %{tl_version}
Provides:       tex(l7xlmtt.fd) = %{tl_version}, tex(l7xlmvtt.fd) = %{tl_version}
Provides:       tex(lmodern.sty) = %{tl_version}, tex(ly1lmdh.fd) = %{tl_version}
Provides:       tex(ly1lmr.fd) = %{tl_version}, tex(ly1lmss.fd) = %{tl_version}
Provides:       tex(ly1lmssq.fd) = %{tl_version}, tex(ly1lmtt.fd) = %{tl_version}
Provides:       tex(ly1lmvtt.fd) = %{tl_version}, tex(omllmm.fd) = %{tl_version}
Provides:       tex(omllmr.fd) = %{tl_version}, tex(omslmr.fd) = %{tl_version}
Provides:       tex(omslmsy.fd) = %{tl_version}, tex(omxlmex.fd) = %{tl_version}
Provides:       tex(ot1lmdh.fd) = %{tl_version}, tex(ot1lmr.fd) = %{tl_version}
Provides:       tex(ot1lmss.fd) = %{tl_version}, tex(ot1lmssq.fd) = %{tl_version}
Provides:       tex(ot1lmtt.fd) = %{tl_version}, tex(ot1lmvtt.fd) = %{tl_version}
Provides:       tex(ot4lmdh.fd) = %{tl_version}, tex(ot4lmr.fd) = %{tl_version}
Provides:       tex(ot4lmss.fd) = %{tl_version}, tex(ot4lmssq.fd) = %{tl_version}
Provides:       tex(ot4lmtt.fd) = %{tl_version}, tex(ot4lmvtt.fd) = %{tl_version}
Provides:       tex(qxlmdh.fd) = %{tl_version}, tex(qxlmr.fd) = %{tl_version}
Provides:       tex(qxlmss.fd) = %{tl_version}, tex(qxlmssq.fd) = %{tl_version}
Provides:       tex(qxlmtt.fd) = %{tl_version}, tex(qxlmvtt.fd) = %{tl_version}
Provides:       tex(t1lmdh.fd) = %{tl_version}, tex(t1lmr.fd) = %{tl_version}
Provides:       tex(t1lmss.fd) = %{tl_version}, tex(t1lmssq.fd) = %{tl_version}
Provides:       tex(t1lmtt.fd) = %{tl_version}, tex(t1lmvtt.fd) = %{tl_version}
Provides:       tex(t5lmdh.fd) = %{tl_version}, tex(t5lmr.fd) = %{tl_version}
Provides:       tex(t5lmss.fd) = %{tl_version}, tex(t5lmssq.fd) = %{tl_version}
Provides:       tex(t5lmtt.fd) = %{tl_version}, tex(t5lmvtt.fd) = %{tl_version}
Provides:       tex(ts1lmdh.fd) = %{tl_version}, tex(ts1lmr.fd) = %{tl_version}
Provides:       tex(ts1lmss.fd) = %{tl_version}, tex(ts1lmssq.fd) = %{tl_version}
Provides:       tex(ts1lmtt.fd) = %{tl_version}, tex(ts1lmvtt.fd) = %{tl_version}

%description -n texlive-lm
The Latin Modern family of fonts consists of 72 text fonts and
20 mathematics fonts, and is based on the Computer Modern fonts
released into public domain by AMS (copyright (c) 1997 AMS).
The lm font set contains a lot of additional characters, mainly
accented ones, but not exclusively. There is one set of fonts,
available both in Adobe Type 1 format (*.pfb) and in OpenType
format (*.otf). There are five sets of TeX Font Metric files,
corresponding to: Cork encoding (cork-*.tfm); QX encoding (qx-
*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); T5
(Vietnamese) encoding (t5-*.tfm); and Text Companion for EC
fonts aka TS1 (ts1-*.tfm).

%package -n texlive-lm-doc
Summary:        Documentation for lm
Version:        svn48145
Provides:       tex-lm-doc
AutoReqProv:    No

%description -n texlive-lm-doc
Documentation for lm

%package -n texlive-lm-math
Provides:       tex-lm-math = %{tl_version}
License:        LPPL
Summary:        OpenType maths fonts for Latin Modern
Version:        svn36915.1.959

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(latinmodern-math.otf) = %{tl_version}

%description -n texlive-lm-math
Latin Modern Math is a maths companion for the Latin Modern
family of fonts, in OpenType format. For use with LuaLaTeX or
XeLaTeX, support is available from the unicode-math package.

%package -n texlive-lm-math-doc
Summary:        Documentation for lm-math
Version:        svn36915.1.959

Provides:       tex-lm-math-doc
AutoReqProv:    No

%description -n texlive-lm-math-doc
Documentation for lm-math

%package -n texlive-lato
Provides:       tex-lato = %{tl_version}
License:        LPPL 1.3
Summary:        Lato font family and LaTeX support
Version:        svn45576
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(keyval.sty)
Requires:       tex(slantsc.sty)
Provides:       tex(lato-01.enc) = %{tl_version}, tex(lato-02.enc) = %{tl_version}
Provides:       tex(lato-dotlessj.enc) = %{tl_version}, tex(lato.map) = %{tl_version}
Provides:       tex(Lato-Bla-01.tfm) = %{tl_version}, tex(Lato-Bla-02.tfm) = %{tl_version}
Provides:       tex(Lato-Bla-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-Bla-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Bla-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-Bla-ot1.tfm) = %{tl_version}, tex(Lato-Bla-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Bla-ts1.tfm) = %{tl_version}, tex(Lato-BlaIta-01.tfm) = %{tl_version}
Provides:       tex(Lato-BlaIta-02.tfm) = %{tl_version}, tex(Lato-BlaIta-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-BlaIta-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-BlaIta-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-BlaIta-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-BlaIta-t1.tfm) = %{tl_version}, tex(Lato-BlaIta-ts1.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-01.tfm) = %{tl_version}, tex(Lato-Bol-02.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-ot1.tfm) = %{tl_version}, tex(Lato-Bol-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Bol-ts1.tfm) = %{tl_version}, tex(Lato-BolIta-01.tfm) = %{tl_version}
Provides:       tex(Lato-BolIta-02.tfm) = %{tl_version}, tex(Lato-BolIta-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-BolIta-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-BolIta-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-BolIta-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-BolIta-t1.tfm) = %{tl_version}, tex(Lato-BolIta-ts1.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-01.tfm) = %{tl_version}, tex(Lato-Hai-02.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-ot1.tfm) = %{tl_version}, tex(Lato-Hai-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Hai-ts1.tfm) = %{tl_version}, tex(Lato-HaiIta-01.tfm) = %{tl_version}
Provides:       tex(Lato-HaiIta-02.tfm) = %{tl_version}, tex(Lato-HaiIta-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-HaiIta-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-HaiIta-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-HaiIta-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-HaiIta-t1.tfm) = %{tl_version}, tex(Lato-HaiIta-ts1.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-01.tfm) = %{tl_version}, tex(Lato-Lig-02.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-ot1.tfm) = %{tl_version}, tex(Lato-Lig-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Lig-ts1.tfm) = %{tl_version}, tex(Lato-LigIta-01.tfm) = %{tl_version}
Provides:       tex(Lato-LigIta-02.tfm) = %{tl_version}, tex(Lato-LigIta-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-LigIta-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-LigIta-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-LigIta-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-LigIta-t1.tfm) = %{tl_version}, tex(Lato-LigIta-ts1.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-01.tfm) = %{tl_version}, tex(Lato-Reg-02.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-ot1.tfm) = %{tl_version}, tex(Lato-Reg-t1.tfm) = %{tl_version}
Provides:       tex(Lato-Reg-ts1.tfm) = %{tl_version}, tex(Lato-RegIta-01.tfm) = %{tl_version}
Provides:       tex(Lato-RegIta-02.tfm) = %{tl_version}, tex(Lato-RegIta-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-RegIta-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Lato-RegIta-dotlessj.tfm) = %{tl_version}
Provides:       tex(Lato-RegIta-ot1.tfm) = %{tl_version}
Provides:       tex(Lato-RegIta-t1.tfm) = %{tl_version}, tex(Lato-RegIta-ts1.tfm) = %{tl_version}
Provides:       tex(Lato-Bla.ttf) = %{tl_version}, tex(Lato-BlaIta.ttf) = %{tl_version}
Provides:       tex(Lato-Bol.ttf) = %{tl_version}, tex(Lato-BolIta.ttf) = %{tl_version}
Provides:       tex(Lato-Hai.ttf) = %{tl_version}, tex(Lato-HaiIta.ttf) = %{tl_version}
Provides:       tex(Lato-Lig.ttf) = %{tl_version}, tex(Lato-LigIta.ttf) = %{tl_version}
Provides:       tex(Lato-Reg.ttf) = %{tl_version}, tex(Lato-RegIta.ttf) = %{tl_version}
Provides:       tex(Lato-Bla-LCDFJ.pfb) = %{tl_version}, tex(Lato-Bla.pfb) = %{tl_version}
Provides:       tex(Lato-BlaIta-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-BlaIta.pfb) = %{tl_version}, tex(Lato-Bol-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-Bol.pfb) = %{tl_version}, tex(Lato-BolIta-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-BolIta.pfb) = %{tl_version}, tex(Lato-Hai-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-Hai.pfb) = %{tl_version}, tex(Lato-HaiIta-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-HaiIta.pfb) = %{tl_version}, tex(Lato-Lig-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-Lig.pfb) = %{tl_version}, tex(Lato-LigIta-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-LigIta.pfb) = %{tl_version}, tex(Lato-Reg-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-Reg.pfb) = %{tl_version}, tex(Lato-RegIta-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Lato-RegIta.pfb) = %{tl_version}, tex(Lato-Bla-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-Bla-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-Bla-ot1.vf) = %{tl_version}, tex(Lato-Bla-t1.vf) = %{tl_version}
Provides:       tex(Lato-Bla-ts1.vf) = %{tl_version}, tex(Lato-BlaIta-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-BlaIta-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-BlaIta-ot1.vf) = %{tl_version}, tex(Lato-BlaIta-t1.vf) = %{tl_version}
Provides:       tex(Lato-BlaIta-ts1.vf) = %{tl_version}, tex(Lato-Bol-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-Bol-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-Bol-ot1.vf) = %{tl_version}, tex(Lato-Bol-t1.vf) = %{tl_version}
Provides:       tex(Lato-Bol-ts1.vf) = %{tl_version}, tex(Lato-BolIta-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-BolIta-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-BolIta-ot1.vf) = %{tl_version}, tex(Lato-BolIta-t1.vf) = %{tl_version}
Provides:       tex(Lato-BolIta-ts1.vf) = %{tl_version}, tex(Lato-Hai-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-Hai-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-Hai-ot1.vf) = %{tl_version}, tex(Lato-Hai-t1.vf) = %{tl_version}
Provides:       tex(Lato-Hai-ts1.vf) = %{tl_version}, tex(Lato-HaiIta-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-HaiIta-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-HaiIta-ot1.vf) = %{tl_version}, tex(Lato-HaiIta-t1.vf) = %{tl_version}
Provides:       tex(Lato-HaiIta-ts1.vf) = %{tl_version}, tex(Lato-Lig-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-Lig-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-Lig-ot1.vf) = %{tl_version}, tex(Lato-Lig-t1.vf) = %{tl_version}
Provides:       tex(Lato-Lig-ts1.vf) = %{tl_version}, tex(Lato-LigIta-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-LigIta-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-LigIta-ot1.vf) = %{tl_version}, tex(Lato-LigIta-t1.vf) = %{tl_version}
Provides:       tex(Lato-LigIta-ts1.vf) = %{tl_version}, tex(Lato-Reg-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-Reg-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-Reg-ot1.vf) = %{tl_version}, tex(Lato-Reg-t1.vf) = %{tl_version}
Provides:       tex(Lato-Reg-ts1.vf) = %{tl_version}, tex(Lato-RegIta-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Lato-RegIta-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Lato-RegIta-ot1.vf) = %{tl_version}, tex(Lato-RegIta-t1.vf) = %{tl_version}
Provides:       tex(Lato-RegIta-ts1.vf) = %{tl_version}, tex(lato.sty) = %{tl_version}
Provides:       tex(ot1fla.fd) = %{tl_version}, tex(t1fla.fd) = %{tl_version}
Provides:       tex(ts1fla.fd) = %{tl_version}

%description -n texlive-lato
Lato is a sanserif typeface family designed in the Summer 2010
by Warsaw-based designer Lukasz Dziedzic for the tyPoland
foundry. This font, which includes five weights (hairline,
light, regular, bold and black), is available from the Google
Font Directory as TrueType files under the Open Font License
version 1.1. The package provides support for this font in
LaTeX. It includes the original TrueType fonts, as well as Type
1 versions, converted for this package using FontForge for full
support with Dvips.

%package -n texlive-lato-doc
Summary:        Documentation for lato
Version:        svn45576
Provides:       tex-lato-doc
AutoReqProv:    No

%description -n texlive-lato-doc
Documentation for lato

%package -n texlive-lfb
Provides:       tex-lfb = %{tl_version}
License:        LPPL
Summary:        A Greek font with normal and bold variants
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lfb10.tfm) = %{tl_version}, tex(lfb11.tfm) = %{tl_version}
Provides:       tex(lfb12.tfm) = %{tl_version}, tex(lfb5.tfm) = %{tl_version}
Provides:       tex(lfb6.tfm) = %{tl_version}, tex(lfb7.tfm) = %{tl_version}
Provides:       tex(lfb8.tfm) = %{tl_version}, tex(lfb9.tfm) = %{tl_version}
Provides:       tex(lfbb10.tfm) = %{tl_version}, tex(lfbb11.tfm) = %{tl_version}
Provides:       tex(lfbb12.tfm) = %{tl_version}, tex(lfbb5.tfm) = %{tl_version}
Provides:       tex(lfbb6.tfm) = %{tl_version}, tex(lfbb7.tfm) = %{tl_version}
Provides:       tex(lfbb8.tfm) = %{tl_version}, tex(lfbb9.tfm) = %{tl_version}

%description -n texlive-lfb
This is a Greek font written in Metafont, with inspiration from
the Bodoni typefaces in old books. It is stylistically a little
more exotic than the standard textbook Greek fonts,
particularly in glyphs like the lowercase rho and kappa. It
aims for a rather calligraphic feel, but seems to blend well
with Computer Modern. There is a ligature scheme which
automatically inserts the breathings required for ancient
texts, making the input text more readable than in some
schemes.

%package -n texlive-lfb-doc
Summary:        Documentation for lfb
Version:        svn15878.1.0

Provides:       tex-lfb-doc
AutoReqProv:    No

%description -n texlive-lfb-doc
Documentation for lfb

%package -n texlive-libertine
Provides:       tex-libertine = %{tl_version}
License:        LPPL
Summary:        Use of Linux Libertine and Biolinum fonts with LaTeX
Version:        svn46211
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(lbtn_25tcsq.enc) = %{tl_version}, tex(lbtn_2exa4z.enc) = %{tl_version}
Provides:       tex(lbtn_2ezly2.enc) = %{tl_version}, tex(lbtn_2jy62z.enc) = %{tl_version}
Provides:       tex(lbtn_2or2lf.enc) = %{tl_version}, tex(lbtn_2xw2fz.enc) = %{tl_version}
Provides:       tex(lbtn_3acize.enc) = %{tl_version}, tex(lbtn_3c7nkx.enc) = %{tl_version}
Provides:       tex(lbtn_3csahh.enc) = %{tl_version}, tex(lbtn_3gqkkc.enc) = %{tl_version}
Provides:       tex(lbtn_3r2fe2.enc) = %{tl_version}, tex(lbtn_4gizrm.enc) = %{tl_version}
Provides:       tex(lbtn_4h5nuw.enc) = %{tl_version}, tex(lbtn_4ifdhd.enc) = %{tl_version}
Provides:       tex(lbtn_4jqvtd.enc) = %{tl_version}, tex(lbtn_4p7cpr.enc) = %{tl_version}
Provides:       tex(lbtn_4pa5s6.enc) = %{tl_version}, tex(lbtn_4qdwcl.enc) = %{tl_version}
Provides:       tex(lbtn_4wvzw4.enc) = %{tl_version}, tex(lbtn_4xgrig.enc) = %{tl_version}
Provides:       tex(lbtn_4zgdm7.enc) = %{tl_version}, tex(lbtn_5t7yy5.enc) = %{tl_version}
Provides:       tex(lbtn_5yotx4.enc) = %{tl_version}, tex(lbtn_64fcpm.enc) = %{tl_version}
Provides:       tex(lbtn_67ud6q.enc) = %{tl_version}, tex(lbtn_6fbtzc.enc) = %{tl_version}
Provides:       tex(lbtn_6icwtb.enc) = %{tl_version}, tex(lbtn_6koeqx.enc) = %{tl_version}
Provides:       tex(lbtn_6mhf45.enc) = %{tl_version}, tex(lbtn_6p6dn5.enc) = %{tl_version}
Provides:       tex(lbtn_75c3wo.enc) = %{tl_version}, tex(lbtn_76gpa5.enc) = %{tl_version}
Provides:       tex(lbtn_77vsbz.enc) = %{tl_version}, tex(lbtn_7aljsl.enc) = %{tl_version}
Provides:       tex(lbtn_7f4ce4.enc) = %{tl_version}, tex(lbtn_7fko2h.enc) = %{tl_version}
Provides:       tex(lbtn_7gfcac.enc) = %{tl_version}, tex(lbtn_7grukw.enc) = %{tl_version}
Provides:       tex(lbtn_7ukmos.enc) = %{tl_version}, tex(lbtn_7yry24.enc) = %{tl_version}
Provides:       tex(lbtn_ac44fr.enc) = %{tl_version}, tex(lbtn_afusau.enc) = %{tl_version}
Provides:       tex(lbtn_agarrr.enc) = %{tl_version}, tex(lbtn_aiatc4.enc) = %{tl_version}
Provides:       tex(lbtn_ashjgg.enc) = %{tl_version}, tex(lbtn_azutla.enc) = %{tl_version}
Provides:       tex(lbtn_b7buxp.enc) = %{tl_version}, tex(lbtn_b7tf5m.enc) = %{tl_version}
Provides:       tex(lbtn_bgokdj.enc) = %{tl_version}, tex(lbtn_bgqvqi.enc) = %{tl_version}
Provides:       tex(lbtn_bkwvsw.enc) = %{tl_version}, tex(lbtn_bvtjwh.enc) = %{tl_version}
Provides:       tex(lbtn_c3m4uk.enc) = %{tl_version}, tex(lbtn_c4mbat.enc) = %{tl_version}
Provides:       tex(lbtn_c6xmqr.enc) = %{tl_version}, tex(lbtn_c6yh3y.enc) = %{tl_version}
Provides:       tex(lbtn_c7kyj5.enc) = %{tl_version}, tex(lbtn_cetbgr.enc) = %{tl_version}
Provides:       tex(lbtn_cg3sqm.enc) = %{tl_version}, tex(lbtn_coqhcm.enc) = %{tl_version}
Provides:       tex(lbtn_crxz7j.enc) = %{tl_version}, tex(lbtn_ctsnwr.enc) = %{tl_version}
Provides:       tex(lbtn_d4efeo.enc) = %{tl_version}, tex(lbtn_d6jdyt.enc) = %{tl_version}
Provides:       tex(lbtn_dc4jmj.enc) = %{tl_version}, tex(lbtn_dgc7p3.enc) = %{tl_version}
Provides:       tex(lbtn_dgwfac.enc) = %{tl_version}, tex(lbtn_dh3kuf.enc) = %{tl_version}
Provides:       tex(lbtn_djk3hd.enc) = %{tl_version}, tex(lbtn_dm3bvq.enc) = %{tl_version}
Provides:       tex(lbtn_dobmnc.enc) = %{tl_version}, tex(lbtn_doxsfd.enc) = %{tl_version}
Provides:       tex(lbtn_drc7cb.enc) = %{tl_version}, tex(lbtn_dylq3g.enc) = %{tl_version}
Provides:       tex(lbtn_e2nnp6.enc) = %{tl_version}, tex(lbtn_ee6wgp.enc) = %{tl_version}
Provides:       tex(lbtn_eesn4m.enc) = %{tl_version}, tex(lbtn_eh2cuc.enc) = %{tl_version}
Provides:       tex(lbtn_ehpgim.enc) = %{tl_version}, tex(lbtn_ek5o26.enc) = %{tl_version}
Provides:       tex(lbtn_etetpy.enc) = %{tl_version}, tex(lbtn_ew6fhv.enc) = %{tl_version}
Provides:       tex(lbtn_ewm74v.enc) = %{tl_version}, tex(lbtn_ezf25l.enc) = %{tl_version}
Provides:       tex(lbtn_f4vjgq.enc) = %{tl_version}, tex(lbtn_f75mth.enc) = %{tl_version}
Provides:       tex(lbtn_fah7mx.enc) = %{tl_version}, tex(lbtn_fdphbq.enc) = %{tl_version}
Provides:       tex(lbtn_ffhb5a.enc) = %{tl_version}, tex(lbtn_g3iycs.enc) = %{tl_version}
Provides:       tex(lbtn_g3y3rv.enc) = %{tl_version}, tex(lbtn_g73f77.enc) = %{tl_version}
Provides:       tex(lbtn_gannye.enc) = %{tl_version}, tex(lbtn_gj2vz5.enc) = %{tl_version}
Provides:       tex(lbtn_gppru4.enc) = %{tl_version}, tex(lbtn_gw5dl2.enc) = %{tl_version}
Provides:       tex(lbtn_gzistf.enc) = %{tl_version}, tex(lbtn_h7zthp.enc) = %{tl_version}
Provides:       tex(lbtn_hj4mhx.enc) = %{tl_version}, tex(lbtn_hk6flg.enc) = %{tl_version}
Provides:       tex(lbtn_hraow7.enc) = %{tl_version}, tex(lbtn_hrou5r.enc) = %{tl_version}
Provides:       tex(lbtn_htcja3.enc) = %{tl_version}, tex(lbtn_hx6qbg.enc) = %{tl_version}
Provides:       tex(lbtn_i5uqjc.enc) = %{tl_version}, tex(lbtn_igd6cx.enc) = %{tl_version}
Provides:       tex(lbtn_ilz2ox.enc) = %{tl_version}, tex(lbtn_imzna7.enc) = %{tl_version}
Provides:       tex(lbtn_indkeb.enc) = %{tl_version}, tex(lbtn_io54zc.enc) = %{tl_version}
Provides:       tex(lbtn_ip3srb.enc) = %{tl_version}, tex(lbtn_iqbcqn.enc) = %{tl_version}
Provides:       tex(lbtn_ism4pi.enc) = %{tl_version}, tex(lbtn_itwafr.enc) = %{tl_version}
Provides:       tex(lbtn_j6rzs3.enc) = %{tl_version}, tex(lbtn_jbwhst.enc) = %{tl_version}
Provides:       tex(lbtn_jk65vs.enc) = %{tl_version}, tex(lbtn_jkqd5u.enc) = %{tl_version}
Provides:       tex(lbtn_jm7hzd.enc) = %{tl_version}, tex(lbtn_jnah33.enc) = %{tl_version}
Provides:       tex(lbtn_jtbvjr.enc) = %{tl_version}, tex(lbtn_jtta5h.enc) = %{tl_version}
Provides:       tex(lbtn_jubyw6.enc) = %{tl_version}, tex(lbtn_jvhpxk.enc) = %{tl_version}
Provides:       tex(lbtn_ka7zfp.enc) = %{tl_version}, tex(lbtn_ki75ao.enc) = %{tl_version}
Provides:       tex(lbtn_kozgsn.enc) = %{tl_version}, tex(lbtn_kuli6n.enc) = %{tl_version}
Provides:       tex(lbtn_kvn6mi.enc) = %{tl_version}, tex(lbtn_l4ygyh.enc) = %{tl_version}
Provides:       tex(lbtn_l5ekfx.enc) = %{tl_version}, tex(lbtn_l7w3c6.enc) = %{tl_version}
Provides:       tex(lbtn_lqfkm2.enc) = %{tl_version}, tex(lbtn_lrrvac.enc) = %{tl_version}
Provides:       tex(lbtn_lu6v53.enc) = %{tl_version}, tex(lbtn_lu7m2n.enc) = %{tl_version}
Provides:       tex(lbtn_m4ul6s.enc) = %{tl_version}, tex(lbtn_m7vdvu.enc) = %{tl_version}
Provides:       tex(lbtn_mdetlm.enc) = %{tl_version}, tex(lbtn_mmutss.enc) = %{tl_version}
Provides:       tex(lbtn_mx3chd.enc) = %{tl_version}, tex(lbtn_mywn7m.enc) = %{tl_version}
Provides:       tex(lbtn_n3ddym.enc) = %{tl_version}, tex(lbtn_n3xw57.enc) = %{tl_version}
Provides:       tex(lbtn_n7uljd.enc) = %{tl_version}, tex(lbtn_naooyc.enc) = %{tl_version}
Provides:       tex(lbtn_ncsllp.enc) = %{tl_version}, tex(lbtn_nh77jq.enc) = %{tl_version}
Provides:       tex(lbtn_nifh3d.enc) = %{tl_version}, tex(lbtn_o3jfbt.enc) = %{tl_version}
Provides:       tex(lbtn_o3v7gd.enc) = %{tl_version}, tex(lbtn_oie7e6.enc) = %{tl_version}
Provides:       tex(lbtn_omcwp2.enc) = %{tl_version}, tex(lbtn_otwoau.enc) = %{tl_version}
Provides:       tex(lbtn_ouu7z6.enc) = %{tl_version}, tex(lbtn_ov2e4f.enc) = %{tl_version}
Provides:       tex(lbtn_owz7oq.enc) = %{tl_version}, tex(lbtn_p657rp.enc) = %{tl_version}
Provides:       tex(lbtn_pagsao.enc) = %{tl_version}, tex(lbtn_pjjyzv.enc) = %{tl_version}
Provides:       tex(lbtn_pjxd67.enc) = %{tl_version}, tex(lbtn_prxh5x.enc) = %{tl_version}
Provides:       tex(lbtn_pwsgbx.enc) = %{tl_version}, tex(lbtn_pznusu.enc) = %{tl_version}
Provides:       tex(lbtn_q2zrjv.enc) = %{tl_version}, tex(lbtn_q6vmp6.enc) = %{tl_version}
Provides:       tex(lbtn_qac756.enc) = %{tl_version}, tex(lbtn_qacof3.enc) = %{tl_version}
Provides:       tex(lbtn_qgimbz.enc) = %{tl_version}, tex(lbtn_qlw4xk.enc) = %{tl_version}
Provides:       tex(lbtn_qwz7uv.enc) = %{tl_version}, tex(lbtn_qzi2b5.enc) = %{tl_version}
Provides:       tex(lbtn_r4tgzq.enc) = %{tl_version}, tex(lbtn_rat5le.enc) = %{tl_version}
Provides:       tex(lbtn_roevjg.enc) = %{tl_version}, tex(lbtn_rvmawp.enc) = %{tl_version}
Provides:       tex(lbtn_s5bq4i.enc) = %{tl_version}, tex(lbtn_sakzps.enc) = %{tl_version}
Provides:       tex(lbtn_sc4wfs.enc) = %{tl_version}, tex(lbtn_sdmuhw.enc) = %{tl_version}
Provides:       tex(lbtn_sfn3yq.enc) = %{tl_version}, tex(lbtn_sjkbhb.enc) = %{tl_version}
Provides:       tex(lbtn_snmbym.enc) = %{tl_version}, tex(lbtn_soyanm.enc) = %{tl_version}
Provides:       tex(lbtn_t62t6h.enc) = %{tl_version}, tex(lbtn_tctjin.enc) = %{tl_version}
Provides:       tex(lbtn_tltjc6.enc) = %{tl_version}, tex(lbtn_tlukpt.enc) = %{tl_version}
Provides:       tex(lbtn_tnngrt.enc) = %{tl_version}, tex(lbtn_txfk5t.enc) = %{tl_version}
Provides:       tex(lbtn_u442ab.enc) = %{tl_version}, tex(lbtn_u7qtuy.enc) = %{tl_version}
Provides:       tex(lbtn_ufdkzv.enc) = %{tl_version}, tex(lbtn_ulngvd.enc) = %{tl_version}
Provides:       tex(lbtn_urpt4g.enc) = %{tl_version}, tex(lbtn_utckyy.enc) = %{tl_version}
Provides:       tex(lbtn_v2xmgd.enc) = %{tl_version}, tex(lbtn_v3uc42.enc) = %{tl_version}
Provides:       tex(lbtn_vezqth.enc) = %{tl_version}, tex(lbtn_vfdxlw.enc) = %{tl_version}
Provides:       tex(lbtn_vm42ve.enc) = %{tl_version}, tex(lbtn_voilzo.enc) = %{tl_version}
Provides:       tex(lbtn_volajt.enc) = %{tl_version}, tex(lbtn_vp3gac.enc) = %{tl_version}
Provides:       tex(lbtn_vpeqwl.enc) = %{tl_version}, tex(lbtn_vsrqlo.enc) = %{tl_version}
Provides:       tex(lbtn_w5h3ip.enc) = %{tl_version}, tex(lbtn_w6afmj.enc) = %{tl_version}
Provides:       tex(lbtn_wcay2e.enc) = %{tl_version}, tex(lbtn_weuxsp.enc) = %{tl_version}
Provides:       tex(lbtn_wfw7lb.enc) = %{tl_version}, tex(lbtn_wnipxy.enc) = %{tl_version}
Provides:       tex(lbtn_wzgokb.enc) = %{tl_version}, tex(lbtn_x4bvel.enc) = %{tl_version}
Provides:       tex(lbtn_xc6c72.enc) = %{tl_version}, tex(lbtn_xeech7.enc) = %{tl_version}
Provides:       tex(lbtn_xogrpz.enc) = %{tl_version}, tex(lbtn_xpavo4.enc) = %{tl_version}
Provides:       tex(lbtn_xsgxhq.enc) = %{tl_version}, tex(lbtn_xz74p6.enc) = %{tl_version}
Provides:       tex(lbtn_xzlo5e.enc) = %{tl_version}, tex(lbtn_y6cxei.enc) = %{tl_version}
Provides:       tex(lbtn_y6gumo.enc) = %{tl_version}, tex(lbtn_yea32d.enc) = %{tl_version}
Provides:       tex(lbtn_yruotg.enc) = %{tl_version}, tex(lbtn_yvenhr.enc) = %{tl_version}
Provides:       tex(lbtn_z254vq.enc) = %{tl_version}, tex(lbtn_zacdtl.enc) = %{tl_version}
Provides:       tex(lbtn_zajy4r.enc) = %{tl_version}, tex(lbtn_zauseh.enc) = %{tl_version}
Provides:       tex(lbtn_zoexom.enc) = %{tl_version}, tex(lbtn_zp73k3.enc) = %{tl_version}
Provides:       tex(lbtn_zq22hj.enc) = %{tl_version}, tex(lbtn_zxvhqu.enc) = %{tl_version}
Provides:       tex(lbtn_zycpkp.enc) = %{tl_version}, tex(lbtn_zyymej.enc) = %{tl_version}
Provides:       tex(libertine.map) = %{tl_version}, tex(LinBiolinum_K.otf) = %{tl_version}
Provides:       tex(LinBiolinum_R.otf) = %{tl_version}, tex(LinBiolinum_RB.otf) = %{tl_version}
Provides:       tex(LinBiolinum_RBO.otf) = %{tl_version}
Provides:       tex(LinBiolinum_RI.otf) = %{tl_version}, tex(LinLibertine_DR.otf) = %{tl_version}
Provides:       tex(LinLibertine_I.otf) = %{tl_version}, tex(LinLibertine_M.otf) = %{tl_version}
Provides:       tex(LinLibertine_MB.otf) = %{tl_version}
Provides:       tex(LinLibertine_MBO.otf) = %{tl_version}
Provides:       tex(LinLibertine_MO.otf) = %{tl_version}
Provides:       tex(LinLibertine_R.otf) = %{tl_version}, tex(LinLibertine_RB.otf) = %{tl_version}
Provides:       tex(LinLibertine_RBI.otf) = %{tl_version}
Provides:       tex(LinLibertine_RI.otf) = %{tl_version}
Provides:       tex(LinLibertine_RZ.otf) = %{tl_version}
Provides:       tex(LinLibertine_RZI.otf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-sup-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-t1.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(LinBiolinumT.pfb) = %{tl_version}, tex(LinBiolinumTB.pfb) = %{tl_version}
Provides:       tex(LinBiolinumTBO.pfb) = %{tl_version}, tex(LinBiolinumTI.pfb) = %{tl_version}
Provides:       tex(LinLibertineDisplayT.pfb) = %{tl_version}
Provides:       tex(LinLibertineIT.pfb) = %{tl_version}, tex(LinLibertineMT.pfb) = %{tl_version}
Provides:       tex(LinLibertineMTB.pfb) = %{tl_version}
Provides:       tex(LinLibertineMTBO.pfb) = %{tl_version}
Provides:       tex(LinLibertineMTO.pfb) = %{tl_version}
Provides:       tex(LinLibertineT.pfb) = %{tl_version}, tex(LinLibertineTB.pfb) = %{tl_version}
Provides:       tex(LinLibertineTBI.pfb) = %{tl_version}
Provides:       tex(LinLibertineTI.pfb) = %{tl_version}, tex(LinLibertineTZ.pfb) = %{tl_version}
Provides:       tex(LinLibertineTZI.pfb) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-sup-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumT-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-sup-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTB-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-sup-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTBO-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-sup-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinBiolinumTI-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineDisplayT-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineIT-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMT-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMT-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTB-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTB-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTBO-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTBO-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTO-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineMTO-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineT-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTB-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTBI-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTI-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZ-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-lf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-sup-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-t1.vf) = %{tl_version}
Provides:       tex(LinLibertineTZI-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LKey.tex) = %{tl_version}, tex(LY1LinuxBiolinumT-LF.fd) = %{tl_version}
Provides:       tex(LY1LinuxBiolinumT-OsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxBiolinumT-Sup.fd) = %{tl_version}
Provides:       tex(LY1LinuxBiolinumT-TLF.fd) = %{tl_version}
Provides:       tex(LY1LinuxBiolinumT-TOsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineDisplayT-LF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineDisplayT-OsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineDisplayT-Sup.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineDisplayT-TLF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineDisplayT-TOsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineInitialsT-LF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineInitialsT-OsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineInitialsT-TLF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineMonoT-Sup.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineMonoT-TLF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineT-Sup.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(LY1LinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(LinBiolinum_K.tex) = %{tl_version}, tex(LinBiolinum_R.tex) = %{tl_version}
Provides:       tex(LinLibertine_I.tex) = %{tl_version}, tex(LinLibertine_R.tex) = %{tl_version}
Provides:       tex(OT1LinuxBiolinumT-LF.fd) = %{tl_version}
Provides:       tex(OT1LinuxBiolinumT-OsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxBiolinumT-Sup.fd) = %{tl_version}
Provides:       tex(OT1LinuxBiolinumT-TLF.fd) = %{tl_version}
Provides:       tex(OT1LinuxBiolinumT-TOsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineDisplayT-LF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineDisplayT-OsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineDisplayT-Sup.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineDisplayT-TLF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineDisplayT-TOsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineInitialsT-LF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineInitialsT-OsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineInitialsT-TLF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineMonoT-Sup.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineMonoT-TLF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineT-Sup.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(OT1LinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(T1LinuxBiolinumT-LF.fd) = %{tl_version}
Provides:       tex(T1LinuxBiolinumT-OsF.fd) = %{tl_version}
Provides:       tex(T1LinuxBiolinumT-Sup.fd) = %{tl_version}
Provides:       tex(T1LinuxBiolinumT-TLF.fd) = %{tl_version}
Provides:       tex(T1LinuxBiolinumT-TOsF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineDisplayT-LF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineDisplayT-OsF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineDisplayT-Sup.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineDisplayT-TLF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineDisplayT-TOsF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineInitialsT-LF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineInitialsT-OsF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineInitialsT-TLF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineMonoT-Sup.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineMonoT-TLF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineT-Sup.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(T1LinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxBiolinumT-LF.fd) = %{tl_version}
Provides:       tex(TS1LinuxBiolinumT-OsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxBiolinumT-TLF.fd) = %{tl_version}
Provides:       tex(TS1LinuxBiolinumT-TOsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineDisplayT-LF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineDisplayT-OsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineDisplayT-TLF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineDisplayT-TOsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineInitialsT-LF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineInitialsT-OsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineInitialsT-TLF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineMonoT-TLF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(TS1LinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(biolinum-type1.sty) = %{tl_version}, tex(biolinum.sty) = %{tl_version}
Provides:       tex(libertine-type1.sty) = %{tl_version}
Provides:       tex(libertine.sty) = %{tl_version}, tex(libertineMono-type1.sty) = %{tl_version}
Provides:       tex(libertineMono.sty) = %{tl_version}, tex(libertineRoman.sty) = %{tl_version}
Provides:       tex(libertineotf.sty) = %{tl_version}

%description -n texlive-libertine
The package provides the Libertine and Biolinum fonts in both
Type 1 and OTF styles, together with support macros for their
use. Monospaced and display fonts, and the "keyboard" set are
also included, in OTF style, only. The mweights package is used
to manage the selection of font weights. The package supersedes
both the libertineotf and the libertine-legacy packages.

%package -n texlive-libertine-doc
Summary:        Documentation for libertine
Version:        svn46211
Provides:       tex-libertine-doc
AutoReqProv:    No

%description -n texlive-libertine-doc
Documentation for libertine

%package -n texlive-librebaskerville
Provides:       tex-librebaskerville = %{tl_version}
License:        LPPL
Summary:        LaTeX support for the Libre Baskerville family of fonts
Version:        svn31741.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(lbsk_5rmxhc.enc) = %{tl_version}, tex(lbsk_7c5ufm.enc) = %{tl_version}
Provides:       tex(lbsk_aprite.enc) = %{tl_version}, tex(lbsk_hguso3.enc) = %{tl_version}
Provides:       tex(lbsk_ktbdpq.enc) = %{tl_version}, tex(lbsk_lbmt7s.enc) = %{tl_version}
Provides:       tex(lbsk_mr5ybw.enc) = %{tl_version}, tex(lbsk_rpuqof.enc) = %{tl_version}
Provides:       tex(lbsk_yeotsr.enc) = %{tl_version}, tex(LibreBaskerville.map) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold.otf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic.otf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic.otf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular.otf) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold.pfb) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic.pfb) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic.pfb) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular.pfb) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBaskerville-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1LibreBaskerville-Sup.fd) = %{tl_version}
Provides:       tex(LY1LibreBaskerville-TLF.fd) = %{tl_version}
Provides:       tex(OT1LibreBaskerville-Sup.fd) = %{tl_version}
Provides:       tex(OT1LibreBaskerville-TLF.fd) = %{tl_version}
Provides:       tex(T1LibreBaskerville-Sup.fd) = %{tl_version}
Provides:       tex(T1LibreBaskerville-TLF.fd) = %{tl_version}
Provides:       tex(TS1LibreBaskerville-TLF.fd) = %{tl_version}
Provides:       tex(librebaskerville.sty) = %{tl_version}

%description -n texlive-librebaskerville
Libre Baskerville is designed by Pablo Impallari. It is
primarily intended to be a web font but is also attractive as a
TeX font. As there is currently no bold italic variant, an
artificially slanted version of the bold variant has been
generated.

%package -n texlive-librebaskerville-doc
Summary:        Documentation for librebaskerville
Version:        svn31741.0

Provides:       tex-librebaskerville-doc
AutoReqProv:    No

%description -n texlive-librebaskerville-doc
Documentation for librebaskerville

%package -n texlive-librecaslon
Provides:       tex-librecaslon = %{tl_version}
License:        OFL
Summary:        Libre Caslon fonts, with LaTeX support
Version:        svn31929.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(lcsl_3cl4ql.enc) = %{tl_version}, tex(lcsl_4g75lz.enc) = %{tl_version}
Provides:       tex(lcsl_5rmxhc.enc) = %{tl_version}, tex(lcsl_aprite.enc) = %{tl_version}
Provides:       tex(lcsl_bpmadw.enc) = %{tl_version}, tex(lcsl_cw7ruh.enc) = %{tl_version}
Provides:       tex(lcsl_hb5o6t.enc) = %{tl_version}, tex(lcsl_klp7zn.enc) = %{tl_version}
Provides:       tex(lcsl_l5dh3w.enc) = %{tl_version}, tex(lcsl_q5us2t.enc) = %{tl_version}
Provides:       tex(lcsl_rpuqof.enc) = %{tl_version}, tex(lcsl_wesofd.enc) = %{tl_version}
Provides:       tex(lcsl_yeotsr.enc) = %{tl_version}, tex(lcsl_ytsyqt.enc) = %{tl_version}
Provides:       tex(lcsl_z4mu2b.enc) = %{tl_version}, tex(LibreCaslon.map) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold.otf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic.otf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic.otf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular.otf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold.pfb) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic.pfb) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic.pfb) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular.pfb) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreCaslonText-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1LibreCaslonText-OsF.fd) = %{tl_version}
Provides:       tex(LY1LibreCaslonText-Sup.fd) = %{tl_version}
Provides:       tex(LY1LibreCaslonText-TLF.fd) = %{tl_version}
Provides:       tex(OT1LibreCaslonText-OsF.fd) = %{tl_version}
Provides:       tex(OT1LibreCaslonText-Sup.fd) = %{tl_version}
Provides:       tex(OT1LibreCaslonText-TLF.fd) = %{tl_version}
Provides:       tex(T1LibreCaslonText-OsF.fd) = %{tl_version}
Provides:       tex(T1LibreCaslonText-Sup.fd) = %{tl_version}
Provides:       tex(T1LibreCaslonText-TLF.fd) = %{tl_version}
Provides:       tex(TS1LibreCaslonText-OsF.fd) = %{tl_version}
Provides:       tex(TS1LibreCaslonText-TLF.fd) = %{tl_version}
Provides:       tex(librecaslon.sty) = %{tl_version}

%description -n texlive-librecaslon
The Libre Caslon fonts are designed by Pablo Impallari.
Although they have been designed for use as web fonts, they
work well as conventional text fonts. A bold italic variant is
not currently available. As a stopgap, an artificially slanted
bold variant has been created and treated as italic.

%package -n texlive-librecaslon-doc
Summary:        Documentation for librecaslon
Version:        svn31929.0

Provides:       tex-librecaslon-doc
AutoReqProv:    No

%description -n texlive-librecaslon-doc
Documentation for librecaslon

%package -n texlive-libris
Provides:       tex-libris = %{tl_version}
License:        GPL+
Summary:        Libris ADF fonts, with LaTeX support
Version:        svn19409.1.007

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(libris-supp.enc) = %{tl_version}, tex(t1-cfr-yly.enc) = %{tl_version}
Provides:       tex(ts1-euro-yly.enc) = %{tl_version}, tex(yly.map) = %{tl_version}
Provides:       tex(ylyb-t1.tfm) = %{tl_version}, tex(ylyb-ts1.tfm) = %{tl_version}
Provides:       tex(ylyb8c.tfm) = %{tl_version}, tex(ylyb8s.tfm) = %{tl_version}
Provides:       tex(ylyb8t.tfm) = %{tl_version}, tex(ylybi-t1.tfm) = %{tl_version}
Provides:       tex(ylybi-ts1.tfm) = %{tl_version}, tex(ylybi8c.tfm) = %{tl_version}
Provides:       tex(ylybi8s.tfm) = %{tl_version}, tex(ylybi8t.tfm) = %{tl_version}
Provides:       tex(ylybiw8t.tfm) = %{tl_version}, tex(ylybw8t.tfm) = %{tl_version}
Provides:       tex(ylyr-t1.tfm) = %{tl_version}, tex(ylyr-ts1.tfm) = %{tl_version}
Provides:       tex(ylyr8c.tfm) = %{tl_version}, tex(ylyr8s.tfm) = %{tl_version}
Provides:       tex(ylyr8t.tfm) = %{tl_version}, tex(ylyri-t1.tfm) = %{tl_version}
Provides:       tex(ylyri-ts1.tfm) = %{tl_version}, tex(ylyri8c.tfm) = %{tl_version}
Provides:       tex(ylyri8s.tfm) = %{tl_version}, tex(ylyri8t.tfm) = %{tl_version}
Provides:       tex(ylyriw8t.tfm) = %{tl_version}, tex(ylyrw8t.tfm) = %{tl_version}
Provides:       tex(ylyb8a.pfb) = %{tl_version}, tex(ylybi8a.pfb) = %{tl_version}
Provides:       tex(ylyr8a.pfb) = %{tl_version}, tex(ylyri8a.pfb) = %{tl_version}
Provides:       tex(ylyb8c.vf) = %{tl_version}, tex(ylyb8t.vf) = %{tl_version}
Provides:       tex(ylybi8c.vf) = %{tl_version}, tex(ylybi8t.vf) = %{tl_version}
Provides:       tex(ylybiw8t.vf) = %{tl_version}, tex(ylybw8t.vf) = %{tl_version}
Provides:       tex(ylyr8c.vf) = %{tl_version}, tex(ylyr8t.vf) = %{tl_version}
Provides:       tex(ylyri8c.vf) = %{tl_version}, tex(ylyri8t.vf) = %{tl_version}
Provides:       tex(ylyriw8t.vf) = %{tl_version}, tex(ylyrw8t.vf) = %{tl_version}
Provides:       tex(libris.sty) = %{tl_version}, tex(t1yly.fd) = %{tl_version}
Provides:       tex(t1ylyw.fd) = %{tl_version}, tex(ts1yly.fd) = %{tl_version}
Provides:       tex(ts1ylyw.fd) = %{tl_version}

%description -n texlive-libris
LibrisADF is a sans-serif family designed to mimic Lydian. The
bundle includes: fonts, in Adobe Type 1, TrueType and OpenType
formats, and LaTeX support macros, for use with the Type 1
versions of the fonts. The LaTeX macros depend on the nfssext-
cfr bundle. GPL licensing applies the fonts themselves; the
support macros are distributed under LPPL licensing.

%package -n texlive-libris-doc
Summary:        Documentation for libris
Version:        svn19409.1.007

Provides:       tex-libris-doc
AutoReqProv:    No

%description -n texlive-libris-doc
Documentation for libris

%package -n texlive-lineara
Provides:       tex-lineara = %{tl_version}
License:        LPPL
Summary:        Linear A script fonts
Version:        svn15878.0
Requires:       texlive-base
Provides:       texlive-linearA = %{tl_version}.1
Obsoletes:      texlive-linearA < %{tl_version}.1, texlive-linearA-fedora-fonts < %{tl_version}.1
Requires:       texlive-kpathsea-bin, tex-kpathsea, texlive-tetex-bin, tex-tetex
Requires:       tex(xspace.sty)
Provides:       tex(linearA.map) = %{tl_version}, tex(LinearA.tfm) = %{tl_version}
Provides:       tex(LinearACmplxSigns.tfm) = %{tl_version}
Provides:       tex(LinearA.pfb) = %{tl_version}, tex(LinearACmplxSigns.pfb) = %{tl_version}
Provides:       tex(linearA.sty) = %{tl_version}

%description -n texlive-lineara
The linearA package provides a simple interface to two fonts
which include all known symbols, simple and complex, of the
Linear A script. This way one can easily replicate Linear A
"texts" using modern typographic technology. Note that the
Linear A script has not been deciphered yet and probably never
will be deciphered.

%package -n texlive-lineara-doc
Summary:        Documentation for linearA
Version:        svn15878.0
Provides:       tex-lineara-doc
AutoReqProv:    No

%description -n texlive-lineara-doc
Documentation for lineara

%package -n texlive-lobster2
Provides:       tex-lobster2 = %{tl_version}
License:        OFL
Summary:        Lobster Two fonts, with support for all LaTeX engines
Version:        svn32617.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(textcomp.sty), tex(xkeyval.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(lbst2_2vl4dw.enc) = %{tl_version}, tex(lbst2_5uiiua.enc) = %{tl_version}
Provides:       tex(lbst2_lyobxw.enc) = %{tl_version}, tex(lbst2_xn7u5r.enc) = %{tl_version}
Provides:       tex(LobsterTwo.map) = %{tl_version}, tex(LobsterTwo-Bold.otf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic.otf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic.otf) = %{tl_version}
Provides:       tex(LobsterTwo-Regular.otf) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ly1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ot1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-t1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ts1.tfm) = %{tl_version}
Provides:       tex(LobsterTwo-Bold.ttf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic.ttf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic.ttf) = %{tl_version}
Provides:       tex(LobsterTwo-Regular.ttf) = %{tl_version}
Provides:       tex(LobsterTwo-Bold.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-Italic.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(LobsterTwo.pfb) = %{tl_version}, tex(LobsterTwoLCDFJ.pfb) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ly1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ot1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-lf-t1.vf) = %{tl_version}
Provides:       tex(LobsterTwo-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1LobsterTwo-LF.fd) = %{tl_version}
Provides:       tex(LobsterTwo.sty) = %{tl_version}, tex(OT1LobsterTwo-LF.fd) = %{tl_version}
Provides:       tex(T1LobsterTwo-LF.fd) = %{tl_version}, tex(TS1LobsterTwo-LF.fd) = %{tl_version}

%description -n texlive-lobster2
Lobster Two is a family of script fonts designed bt Pablo
Impallari. It has many ligatures and terminal forms, but most
of these can be accessed only using XeLaTeX or LuaLaTeX. Font
access and use is supported in LaTeX.

%package -n texlive-lobster2-doc
Summary:        Documentation for lobster2
Version:        svn32617.0

Provides:       tex-lobster2-doc
AutoReqProv:    No

%description -n texlive-lobster2-doc
Documentation for lobster2

%package -n texlive-lxfonts
Provides:       tex-lxfonts = %{tl_version}
License:        LPPL
Summary:        Set of slide fonts based on CM
Version:        svn32354.2.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(etoolbox.sty)
Provides:       tex(lxfonts.map) = %{tl_version}, tex(lcmbsy8.tfm) = %{tl_version}
Provides:       tex(lcmex8.tfm) = %{tl_version}, tex(lcmmi8.tfm) = %{tl_version}
Provides:       tex(lcmmib8.tfm) = %{tl_version}, tex(lcmsy8.tfm) = %{tl_version}
Provides:       tex(leclb8.tfm) = %{tl_version}, tex(lecli8.tfm) = %{tl_version}
Provides:       tex(leclo8.tfm) = %{tl_version}, tex(leclq8.tfm) = %{tl_version}
Provides:       tex(llasy8.tfm) = %{tl_version}, tex(llasyb8.tfm) = %{tl_version}
Provides:       tex(llcmss8.tfm) = %{tl_version}, tex(llcmssb8.tfm) = %{tl_version}
Provides:       tex(llcmssi8.tfm) = %{tl_version}, tex(llcmsso8.tfm) = %{tl_version}
Provides:       tex(lmsam8.tfm) = %{tl_version}, tex(lmsbm8.tfm) = %{tl_version}
Provides:       tex(ltclb8.tfm) = %{tl_version}, tex(ltcli8.tfm) = %{tl_version}
Provides:       tex(ltclo8.tfm) = %{tl_version}, tex(ltclq8.tfm) = %{tl_version}
Provides:       tex(lcmbsy8.pfb) = %{tl_version}, tex(lcmex8.pfb) = %{tl_version}
Provides:       tex(lcmmi8.pfb) = %{tl_version}, tex(lcmmib8.pfb) = %{tl_version}
Provides:       tex(lcmsy8.pfb) = %{tl_version}, tex(leclb8.pfb) = %{tl_version}
Provides:       tex(lecli8.pfb) = %{tl_version}, tex(leclo8.pfb) = %{tl_version}
Provides:       tex(leclq8.pfb) = %{tl_version}, tex(llasy8.pfb) = %{tl_version}
Provides:       tex(llasyb8.pfb) = %{tl_version}, tex(llcmss8.pfb) = %{tl_version}
Provides:       tex(llcmssb8.pfb) = %{tl_version}, tex(llcmssi8.pfb) = %{tl_version}
Provides:       tex(llcmsso8.pfb) = %{tl_version}, tex(lmsam8.pfb) = %{tl_version}
Provides:       tex(lmsbm8.pfb) = %{tl_version}, tex(ltclb8.pfb) = %{tl_version}
Provides:       tex(ltcli8.pfb) = %{tl_version}, tex(ltclo8.pfb) = %{tl_version}
Provides:       tex(ltclq8.pfb) = %{tl_version}, tex(lgrllcmss.fd) = %{tl_version}
Provides:       tex(lgrllcmtt.fd) = %{tl_version}, tex(lxfonts.sty) = %{tl_version}
Provides:       tex(omlllcmm.fd) = %{tl_version}, tex(omsllcmsy.fd) = %{tl_version}
Provides:       tex(omxllcmex.fd) = %{tl_version}, tex(ot1llcmss.fd) = %{tl_version}
Provides:       tex(ot1llcmtt.fd) = %{tl_version}, tex(t1llcmss.fd) = %{tl_version}
Provides:       tex(t1llcmtt.fd) = %{tl_version}, tex(ts1llcmss.fd) = %{tl_version}
Provides:       tex(ulllasy.fd) = %{tl_version}, tex(ulmsa.fd) = %{tl_version}
Provides:       tex(ulmsb.fd) = %{tl_version}

%description -n texlive-lxfonts
The bundle contains the traditional slides fonts revised to be
completely usable both as text fonts and mathematics fonts;
they are fully integrate with the new operators, letters,
symbols and extensible delimiter fonts, as well as with the AMS
fonts, all redone with the same stylistic parameters.

%package -n texlive-lxfonts-doc
Summary:        Documentation for lxfonts
Version:        svn32354.2.0b

Provides:       tex-lxfonts-doc
AutoReqProv:    No

%description -n texlive-lxfonts-doc
Documentation for lxfonts

%package -n texlive-ly1
Provides:       tex-ly1 = %{tl_version}
License:        LPPL
Summary:        Support for LY1 LaTeX encoding
Version:        svn47848
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(texnansi.enc) = %{tl_version}, tex(pag8y.map) = %{tl_version}
Provides:       tex(pbk8y.map) = %{tl_version}, tex(pcr8y.map) = %{tl_version}
Provides:       tex(phv8y.map) = %{tl_version}, tex(pnc8y.map) = %{tl_version}
Provides:       tex(ppl8y.map) = %{tl_version}, tex(ptm8y.map) = %{tl_version}
Provides:       tex(pzc8y.map) = %{tl_version}, tex(pagd8y.tfm) = %{tl_version}
Provides:       tex(pagdo8y.tfm) = %{tl_version}, tex(pagk8y.tfm) = %{tl_version}
Provides:       tex(pagko8y.tfm) = %{tl_version}, tex(pbkd8y.tfm) = %{tl_version}
Provides:       tex(pbkdi8y.tfm) = %{tl_version}, tex(pbkdo8y.tfm) = %{tl_version}
Provides:       tex(pbkl8y.tfm) = %{tl_version}, tex(pbkli8y.tfm) = %{tl_version}
Provides:       tex(pbklo8y.tfm) = %{tl_version}, tex(pcrb8y.tfm) = %{tl_version}
Provides:       tex(pcrbo8y.tfm) = %{tl_version}, tex(pcrr8y.tfm) = %{tl_version}
Provides:       tex(pcrro8y.tfm) = %{tl_version}, tex(phvb8y.tfm) = %{tl_version}
Provides:       tex(phvb8yn.tfm) = %{tl_version}, tex(phvbo8y.tfm) = %{tl_version}
Provides:       tex(phvbo8yn.tfm) = %{tl_version}, tex(phvr8y.tfm) = %{tl_version}
Provides:       tex(phvr8yn.tfm) = %{tl_version}, tex(phvro8y.tfm) = %{tl_version}
Provides:       tex(phvro8yn.tfm) = %{tl_version}, tex(pncb8y.tfm) = %{tl_version}
Provides:       tex(pncbi8y.tfm) = %{tl_version}, tex(pncbo8y.tfm) = %{tl_version}
Provides:       tex(pncr8y.tfm) = %{tl_version}, tex(pncri8y.tfm) = %{tl_version}
Provides:       tex(pncro8y.tfm) = %{tl_version}, tex(pplb8y.tfm) = %{tl_version}
Provides:       tex(pplbi8y.tfm) = %{tl_version}, tex(pplbo8y.tfm) = %{tl_version}
Provides:       tex(pplbu8y.tfm) = %{tl_version}, tex(pplr8y.tfm) = %{tl_version}
Provides:       tex(pplr8yn.tfm) = %{tl_version}, tex(pplri8y.tfm) = %{tl_version}
Provides:       tex(pplro8y.tfm) = %{tl_version}, tex(pplrr8ye.tfm) = %{tl_version}
Provides:       tex(pplru8y.tfm) = %{tl_version}, tex(ptmb8y.tfm) = %{tl_version}
Provides:       tex(ptmbc8y.tfm) = %{tl_version}, tex(ptmbi8y.tfm) = %{tl_version}
Provides:       tex(ptmbo8y.tfm) = %{tl_version}, tex(ptmr8y.tfm) = %{tl_version}
Provides:       tex(ptmr8yn.tfm) = %{tl_version}, tex(ptmrc8y.tfm) = %{tl_version}
Provides:       tex(ptmri8y.tfm) = %{tl_version}, tex(ptmro8y.tfm) = %{tl_version}
Provides:       tex(ptmrr8ye.tfm) = %{tl_version}, tex(pzcmi8y.tfm) = %{tl_version}
Provides:       tex(ptmbc8y.vf) = %{tl_version}, tex(ptmrc8y.vf) = %{tl_version}
Provides:       tex(ly1enc.def) = %{tl_version}, tex(ly1pag.fd) = %{tl_version}
Provides:       tex(ly1pbk.fd) = %{tl_version}, tex(ly1pcr.fd) = %{tl_version}
Provides:       tex(ly1phv.fd) = %{tl_version}, tex(ly1pnc.fd) = %{tl_version}
Provides:       tex(ly1ppl.fd) = %{tl_version}, tex(ly1ptm.fd) = %{tl_version}
Provides:       tex(ly1pzc.fd) = %{tl_version}, tex(texnansi.sty) = %{tl_version}
Provides:       tex(texnansi.tex) = %{tl_version}

%description -n texlive-ly1
The Y&Y 'texnansi' (TeX and ANSI, for Microsoft interpretations
of ANSI standards) encoding lives on, even after the decease of
the company; it is known in the LaTeX scheme of things as LY1
encoding. This bundle includes metrics and LaTeX macros to use
the basic three (Times, Helvetica and Courier) Adobe Type 1
fonts in LaTeX using LY1 encoding.

%package -n texlive-ly1-doc
Summary:        Documentation for ly1
Version:        svn47848
Provides:       tex-ly1-doc
AutoReqProv:    No

%description -n texlive-ly1-doc
Documentation for ly1

%package -n texlive-labyrinth
Provides:       tex-labyrinth = %{tl_version}
License:        LPPL
Summary:        Draw labyrinths and solution paths
Version:        svn33454.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(xkeyval.sty), tex(picture.sty)
Provides:       tex(labyrinth.sty) = %{tl_version}

%description -n texlive-labyrinth
The labyrinth package provides code and an environment for
typesetting simple labyrinths with LaTeX, and generating an
automatic or manual solution path.

%package -n texlive-labyrinth-doc
Summary:        Documentation for labyrinth
Version:        svn33454.1.0

Provides:       tex-labyrinth-doc
AutoReqProv:    No

%description -n texlive-labyrinth-doc
Documentation for labyrinth

%package -n texlive-logicpuzzle
Provides:       tex-logicpuzzle = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset (grid-based) logic puzzles
Version:        svn34491.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(ifthen.sty), tex(ragged2e.sty), tex(marginnote.sty)
Requires:       tex(tikz.sty)
Provides:       tex(logicpuzzle.sty) = %{tl_version}, tex(lpenv.sty) = %{tl_version}

%description -n texlive-logicpuzzle
The package allows the user to typeset various logic puzzles.
At the moment the following puzzles are supported: 2D-Sudoku
(aka Magiequadrat, Diagon, ...), Battleship (aka Bimaru,
Marinespiel, Batalla Naval, ...), Bokkusu (aka Kakurasu,
Feldersummenratsel, ...), Bridges (akak Bruckenbau, Hashi,
...), Chaos Sudoku, Four Winds (aka Eminent Domain,
Lichtstrahl, ...), Hakyuu (aka Seismic, Ripple Effect, ...),
Hitori, Kakuro, Kendoku (aka Mathdoku, Calcudoku, Basic,
MiniPlu, Ken Ken, Square Wisdom, Sukendo, Caldoku, ..., Killer
Sudoku (aka Samunapure, Sum Number Place, Sumdoku,
Gebietssummen, ...), Laser Beam (aka Laserstrahl, ...), Magic
Labyrinth (aka Magic Spiral, Magisches Labyrinth, ...), Magnets
(aka Magnetplatte, Magnetfeld, ...), Masyu (aka Mashi,
{White|Black} Pearls, ...), Minesweeper (aka Minensuche, ...),
Nonogram (aka Griddlers, Hanjie, Tsunami, Logic Art, Logimage,
...), Number Link (aka Alphabet Link, Arukone, Buchstabenbund,
...), Resuko, Schatzsuche, Skyline (aka Skycrapers,
Wolkenkratzer, Hochhauser, ...), including Skyline Sudoku and
Skyline Sudoku (N*N) variants, Slitherlink (aka Fences, Number
Line, Dotty Dilemma, Sli-Lin, Takegaki, Great Wall of China,
Loop the Loop, Rundweg, Gartenzaun, ...), Star Battle (aka
Sternenschlacht, ...), Stars and Arrows (aka Sternenhimmel,
...), Sudoku, Sun and Moon (aka Sternenhaufen, Munraito, ...),
Tents and Trees (aka Zeltlager, Zeltplatz, Camping, ...), and
Tunnel.

%package -n texlive-logicpuzzle-doc
Summary:        Documentation for logicpuzzle
Version:        svn34491.2.5

Provides:       tex-logicpuzzle-doc
AutoReqProv:    No

%description -n texlive-logicpuzzle-doc
Documentation for logicpuzzle

%package -n texlive-lambda-lists
Provides:       tex-lambda-lists = %{tl_version}
License:        LPPL
Summary:        Lists in TeX's mouth
Version:        svn31402.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lambda.sty) = %{tl_version}

%description -n texlive-lambda-lists
These list-processing macros avoid the reassignments employed
in the macros shown in Appendix D of the TeXbook: all the
manipulations take place in what Knuth is pleased to call
"TeX's mouth".

%package -n texlive-lambda-lists-doc
Summary:        Documentation for lambda-lists
Version:        svn31402.0

Provides:       tex-lambda-lists-doc
AutoReqProv:    No

%description -n texlive-lambda-lists-doc
Documentation for lambda-lists

%package -n texlive-langcode
Provides:       tex-langcode = %{tl_version}
License:        LPPL 1.3
Summary:        Simple language-dependent settings based on language codes
Version:        svn27764.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(dowith.sty), tex(dhua.sty)
Provides:       tex(langcode.sty) = %{tl_version}

%description -n texlive-langcode
The package provides a command \uselangcode{<code>} to adjust
language-dependent settings such as key words, typographical
conventions and language codes (ISO 639-1). The package
provides a means of selecting macros according to the specified
code, for preparing a document that is to be separately typeset
in different laguages. The package is dependent on the plainpkg
package, and is already in use in the morehype and catcodes
packages.

%package -n texlive-langcode-doc
Summary:        Documentation for langcode
Version:        svn27764.0.2

Provides:       tex-langcode-doc
AutoReqProv:    No

%description -n texlive-langcode-doc
Documentation for langcode

%package -n texlive-lecturer
Provides:       tex-lecturer = %{tl_version}
License:        LPPL
Summary:        On-screen presentations for (almost) all formats
Version:        svn23916.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lecturer.sty) = %{tl_version}, tex(lecturer.tex) = %{tl_version}
Provides:       tex(ltr-areas.tex) = %{tl_version}, tex(ltr-graphics.tex) = %{tl_version}
Provides:       tex(ltr-job.tex) = %{tl_version}, tex(ltr-navigation.tex) = %{tl_version}
Provides:       tex(ltr-slides.tex) = %{tl_version}, tex(ltr-steps.tex) = %{tl_version}
Provides:       tex(t-lecturer.tex) = %{tl_version}

%description -n texlive-lecturer
The package creates slides for on-screen presentations based on
PDF features without manipulating TeX's typesetting process.
The presentation flow relies on PDF's abilities to display
content step by step. Features include: Free positioning of
anything anywhere in painted areas on the slide, as well as in
the main textblock; Numerous attributes to control the layout
and the presentation flow, from TeX's primitive dimensions to
the visibility of steps; Feature inheritance from global to
local settings, with intermediate types; Basic drawing
facilities to produce symbols, e.g., for list items or buttons;
Colours, transparency, shades, and pictures; Navigation with
links, pop-up menus, and customizable bookmarks; Easy switch
between presentation and handout; and PDF transitions. Besides
the traditional documentation, the distribution includes visual
documentation and six demo presentations ranging from geometric
abstraction to classic style to silly video game. Lecturer is
designed to work with all formats, but presently fails with
ConTeXt MkIV (because of clashes in management of PDF objects,
probably), works only with pdfTeX and LuaTeX for the time
being, and requires texapi and yax, both v.1.02.

%package -n texlive-lecturer-doc
Summary:        Documentation for lecturer
Version:        svn23916.0

Provides:       tex-lecturer-doc
AutoReqProv:    No

%description -n texlive-lecturer-doc
Documentation for lecturer

%package -n texlive-librarian
Provides:       tex-librarian = %{tl_version}
License:        LPPL
Summary:        Tools to create bibliographies in TeX
Version:        svn19880.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(librarian.sty) = %{tl_version}, tex(librarian.tex) = %{tl_version}
Provides:       tex(t-librarian.tex) = %{tl_version}

%description -n texlive-librarian
The package extracts information in bib files, makes it
available in the current document, and sorts lists of entries
according to that information and the user's specifications.
Citation and bibliography styles can then be written directly
in TeX, without any use of BibTeX. Creating references thus
depends entirely on the user's skill in TeX. The package works
with all formats that use plain TeX's basic syntactic sugar;
the distribution includes a third-party file for ConTeXt and a
style file for LaTeX. As an example of use, an Author (Year)
style is given in a separate file and explained in the
documentation.

%package -n texlive-librarian-doc
Summary:        Documentation for librarian
Version:        svn19880.1.0

Provides:       tex-librarian-doc
AutoReqProv:    No

%description -n texlive-librarian-doc
Documentation for librarian

%package -n texlive-ledmac
Provides:       tex-ledmac = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset scholarly editions
Version:        svn41811
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(afoot.sty) = %{tl_version}, tex(ledarab.sty) = %{tl_version}
Provides:       tex(ledmac.sty) = %{tl_version}, tex(ledpar.sty) = %{tl_version}

%description -n texlive-ledmac
A macro package for typesetting scholarly critical editions.
The ledmac package is a LaTeX port of the plain TeX EDMAC
macros. It supports indexing by page and line number and simple
tabular- and array-style environments. The package is
distributed with the related ledpar and ledarab packages. The
package is now superseded by eledmac.

%package -n texlive-ledmac-doc
Summary:        Documentation for ledmac
Version:        svn41811
Provides:       tex-ledmac-doc
AutoReqProv:    No

%description -n texlive-ledmac-doc
Documentation for ledmac

%package -n texlive-leipzig
Provides:       tex-leipzig = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset and index linguistic gloss abbreviations
Version:        svn44625
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(leipzig.sty) = %{tl_version}, tex(leipzig.tex) = %{tl_version}

%description -n texlive-leipzig
The leipzig package provides a set of macros for standard
glossing abbreviations, with options to create new ones. They
are mnemonic (e.g. \Acc{} for accusative, abbreviated acc).
These abbre can be used alone or on top of the glossaries
package for easy indexing and glossary printing.

%package -n texlive-leipzig-doc
Summary:        Documentation for leipzig
Version:        svn44625
Provides:       tex-leipzig-doc
AutoReqProv:    No

%description -n texlive-leipzig-doc
Documentation for leipzig

%package -n texlive-lexref
Provides:       tex-lexref = %{tl_version}
License:        LPPL 1.3
Summary:        Convenient and uniform references to legal provisions
Version:        svn36026.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(xargs.sty), tex(xstring.sty), tex(nomencl.sty)
Requires:       tex(splitidx.sty), tex(ifthen.sty), tex(stringstrings.sty)
Provides:       tex(lexref.sty) = %{tl_version}

%description -n texlive-lexref
The package is aimed at continental lawyers (especially those
in Switzerland and Germany), allowing the user to make
references to legal provisions conveniently and uniformly. The
package also allows the user to add cited Acts to a
nomenclature list (automatically), and to build specific
indexes for each cited Act. The package is still under
development, and should be treated as an 'alpha'-release.

%package -n texlive-lexref-doc
Summary:        Documentation for lexref
Version:        svn36026.1.1a

Provides:       tex-lexref-doc
AutoReqProv:    No

%description -n texlive-lexref-doc
Documentation for lexref

%package -n texlive-linguex
Provides:       tex-linguex = %{tl_version}
License:        LPPL
Summary:        Format linguists' examples
Version:        svn30815.4.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(cgloss4e.sty), tex(tree-dvips.sty)
Provides:       tex(linguex.sty) = %{tl_version}, tex(linguho.sty) = %{tl_version}
Provides:       tex(lingo.sty) = %{tl_version}, tex(ps-trees.sty) = %{tl_version}

%description -n texlive-linguex
This bundle comprises two packages: The linguex package
facilitates the formatting of linguist examples, automatically
taking care of example numbering, indentations, indexed
brackets, and the '*' in grammaticality judgments. The ps-trees
package provides linguistic trees, building on the macros of
tree-dvips, but overcoming some of the older package's
shortcomings.

%package -n texlive-linguex-doc
Summary:        Documentation for linguex
Version:        svn30815.4.3

Provides:       tex-linguex-doc
AutoReqProv:    No

%description -n texlive-linguex-doc
Documentation for linguex

%package -n texlive-liturg
Provides:       tex-liturg = %{tl_version}
License:        LPPL
Summary:        Support for typesetting Catholic liturgical texts
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty), tex(color.sty), tex(lettrine.sty), tex(ecclesiastic.sty)
Provides:       tex(liturg.sty) = %{tl_version}

%description -n texlive-liturg
The packages offers simple macros for typesetting Catholic
liturgical texts, particularly Missal and Breviary texts. The
package assumes availability of Latin typesetting packages.

%package -n texlive-liturg-doc
Summary:        Documentation for liturg
Version:        svn15878.1.0

Provides:       tex-liturg-doc
AutoReqProv:    No

%description -n texlive-liturg-doc
Documentation for liturg

%package -n texlive-lshort-persian-doc
Summary:        Documentation for lshort-persian
Version:        svn31296.5.01

Provides:       tex-lshort-persian-doc
AutoReqProv:    No

%description -n texlive-lshort-persian-doc
Documentation for lshort-persian

%package -n texlive-latex-notes-zh-cn-doc
Summary:        Documentation for latex-notes-zh-cn
Version:        svn15878.1.20

Provides:       tex-latex-notes-zh-cn-doc
AutoReqProv:    No

%description -n texlive-latex-notes-zh-cn-doc
Documentation for latex-notes-zh-cn

%package -n texlive-lshort-chinese-doc
Summary:        Documentation for lshort-chinese
Version:        svn43606
Provides:       tex-lshort-chinese-doc
AutoReqProv:    No

%description -n texlive-lshort-chinese-doc
Documentation for lshort-chinese

%package -n texlive-lcyw
Provides:       tex-lcyw = %{tl_version}
License:        LPPL 1.3
Summary:        Make Classic Cyrillic CM fonts accessible in LaTeX
Version:        svn15878.v1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty)
Provides:       tex(cmap-cyr-vf.sty) = %{tl_version}, tex(lcywcmr.fd) = %{tl_version}
Provides:       tex(lcywcmss.fd) = %{tl_version}, tex(lcywcmssq.fd) = %{tl_version}
Provides:       tex(lcywcmtt.fd) = %{tl_version}, tex(lcywenc.def) = %{tl_version}

%description -n texlive-lcyw
The package makes the classic CM Cyrillic fonts accessible for
use with LaTeX.

%package -n texlive-lcyw-doc
Summary:        Documentation for lcyw
Version:        svn15878.v1.1

Provides:       tex-lcyw-doc
AutoReqProv:    No

%description -n texlive-lcyw-doc
Documentation for lcyw

%package -n texlive-lh
Provides:       tex-lh = %{tl_version}
License:        LPPL
Summary:        Cyrillic fonts that support LaTeX standard encodings
Version:        svn15878.3.5g

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-ec
Provides:       tex(lh-lcy.sty) = %{tl_version}, tex(lh-lcyccr.sty) = %{tl_version}
Provides:       tex(lh-lcyxccr.sty) = %{tl_version}, tex(lh-ot2.sty) = %{tl_version}
Provides:       tex(lh-ot2ccr.sty) = %{tl_version}, tex(lh-ot2xccr.sty) = %{tl_version}
Provides:       tex(lh-t2accr.sty) = %{tl_version}, tex(lh-t2axccr.sty) = %{tl_version}
Provides:       tex(lh-t2bccr.sty) = %{tl_version}, tex(lh-t2bxccr.sty) = %{tl_version}
Provides:       tex(lh-t2cccr.sty) = %{tl_version}, tex(lh-t2cxccr.sty) = %{tl_version}
Provides:       tex(lh-x2ccr.sty) = %{tl_version}, tex(lh-x2xccr.sty) = %{tl_version}
Provides:       tex(nfssfox.tex) = %{tl_version}, tex(testfox.tex) = %{tl_version}
Provides:       tex(testkern.tex) = %{tl_version}

%description -n texlive-lh
The LH fonts address the problem of the wide variety of
alphabets that are written with Cyrillic-style characters. The
fonts are the original basis of the set of T2* and X2 encodings
that are now used when LaTeX users need to write in Cyrillic
languages. Macro support in standard LaTeX encodings is offered
through the cyrillic and t2 bundles, and the package itself
offers support for other (more traditional) encodings. The
fonts, in the standard T2* and X2 encodings are available in
Adobe Type 1 format, in the CM-Super family of fonts. The
package also offers its own LaTeX support for OT2 encoded
fonts, CM bright shaped fonts and Concrete shaped fonts.

%package -n texlive-lh-doc
Summary:        Documentation for lh
Version:        svn15878.3.5g

Provides:       tex-lh-doc
AutoReqProv:    No
Requires:       tex-ec-doc

%description -n texlive-lh-doc
Documentation for lh

%package -n texlive-lhcyr
Provides:       tex-lhcyr = %{tl_version}
License:        Lhcyr
Summary:        A non-standard Cyrillic input scheme
Version:        svn31795.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(karabas.tex) = %{tl_version}, tex(kniga.tex) = %{tl_version}
Provides:       tex(lhcyralt-hyphen.cfg) = %{tl_version}
Provides:       tex(lhcyralt-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyralt.sty) = %{tl_version}, tex(ot1lhdh.fd) = %{tl_version}
Provides:       tex(ot1lhfib.fd) = %{tl_version}, tex(ot1lhfr.fd) = %{tl_version}
Provides:       tex(ot1lhr.fd) = %{tl_version}, tex(ot1lhss.fd) = %{tl_version}
Provides:       tex(ot1lhtt.fd) = %{tl_version}, tex(ot1lhvtt.fd) = %{tl_version}
Provides:       tex(lhcyrkoi-hyphen.cfg) = %{tl_version}
Provides:       tex(lhcyrkoi-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrkoi.sty) = %{tl_version}, tex(ot1kcdh.fd) = %{tl_version}
Provides:       tex(ot1kcfib.fd) = %{tl_version}, tex(ot1kcfr.fd) = %{tl_version}
Provides:       tex(ot1kcr.fd) = %{tl_version}, tex(ot1kcss.fd) = %{tl_version}
Provides:       tex(ot1kctt.fd) = %{tl_version}, tex(ot1kcvtt.fd) = %{tl_version}
Provides:       tex(lhcyrwin-hyphen.cfg) = %{tl_version}
Provides:       tex(lhcyrwin-rhyphen.tex) = %{tl_version}
Provides:       tex(lhcyrwin.sty) = %{tl_version}, tex(ot1wcdh.fd) = %{tl_version}
Provides:       tex(ot1wcfib.fd) = %{tl_version}, tex(ot1wcfr.fd) = %{tl_version}
Provides:       tex(ot1wcr.fd) = %{tl_version}, tex(ot1wcss.fd) = %{tl_version}
Provides:       tex(ot1wctt.fd) = %{tl_version}, tex(ot1wcvtt.fd) = %{tl_version}
Provides:       tex(otchet.tex) = %{tl_version}, tex(pismo.tex) = %{tl_version}
Provides:       tex(rusfonts.tex) = %{tl_version}, tex(statya.tex) = %{tl_version}

%description -n texlive-lhcyr
A collection of three LaTeX 2e styles intended for typesetting
Russian and bilingual English-Russian documents, using the lh
fonts and without the benefit of babel's language-switching
mechanisms. The packages (lhcyralt and lhcyrwin for use under
emTeX, and lhcyrkoi for use under teTeX) provide mappings
between the input encoding and the font encoding (which is
described as OT1). The way this is done does not match the way
inputenc would do the job, for output via fontenc to one of the
T2 series of font encodings.

%package -n texlive-lshort-bulgarian-doc
Summary:        Documentation for lshort-bulgarian
Version:        svn15878.0

Provides:       tex-lshort-bulgarian-doc
AutoReqProv:    No

%description -n texlive-lshort-bulgarian-doc
Documentation for lshort-bulgarian

%package -n texlive-lshort-mongol-doc
Summary:        Documentation for lshort-mongol
Version:        svn15878.4.26

Provides:       tex-lshort-mongol-doc
AutoReqProv:    No

%description -n texlive-lshort-mongol-doc
Documentation for lshort-mongol

%package -n texlive-lshort-russian-doc
Summary:        Documentation for lshort-russian
Version:        svn18906.0

Provides:       tex-lshort-russian-doc
AutoReqProv:    No

%description -n texlive-lshort-russian-doc
Documentation for lshort-russian

%package -n texlive-lshort-ukr-doc
Summary:        Documentation for lshort-ukr
Version:        svn15878.4.00

Provides:       tex-lshort-ukr-doc
AutoReqProv:    No

%description -n texlive-lshort-ukr-doc
Documentation for lshort-ukr

%package -n texlive-lshort-czech-doc
Summary:        Documentation for lshort-czech
Version:        svn29803.4.27

Provides:       tex-lshort-czech-doc
AutoReqProv:    No

%description -n texlive-lshort-czech-doc
Documentation for lshort-czech

%package -n texlive-lshort-slovak-doc
Summary:        Documentation for lshort-slovak
Version:        svn15878.0

Provides:       tex-lshort-slovak-doc
AutoReqProv:    No

%description -n texlive-lshort-slovak-doc
Documentation for lshort-slovak


%package -n texlive-l2tabu-english-doc
Summary:        Documentation for l2tabu-english
Version:        svn15878.1.8.5.7

Provides:       tex-l2tabu-english-doc
AutoReqProv:    No

%description -n texlive-l2tabu-english-doc
Documentation for l2tabu-english

%package -n texlive-latex-brochure-doc
Summary:        Documentation for latex-brochure
Version:        svn40612

Provides:       tex-latex-brochure-doc
AutoReqProv:    No

%description -n texlive-latex-brochure-doc
Documentation for latex-brochure

%package -n texlive-latex-course-doc
Summary:        Documentation for latex-course
Version:        svn25505.2

Provides:       tex-latex-course-doc
AutoReqProv:    No

%description -n texlive-latex-course-doc
Documentation for latex-course

%package -n texlive-latex-doc-ptr-doc
Summary:        Documentation for latex-doc-ptr
Version:        svn15878.0

Provides:       tex-latex-doc-ptr-doc
AutoReqProv:    No

%description -n texlive-latex-doc-ptr-doc
Documentation for latex-doc-ptr

%package -n texlive-latex-graphics-companion-doc
Summary:        Documentation for latex-graphics-companion
Version:        svn29235.0

Provides:       tex-latex-graphics-companion-doc
AutoReqProv:    No

%description -n texlive-latex-graphics-companion-doc
Documentation for latex-graphics-companion

%package -n texlive-latex-veryshortguide-doc
Summary:        Documentation for latex-veryshortguide
Version:        svn41844
Provides:       tex-latex-veryshortguide-doc
AutoReqProv:    No

%description -n texlive-latex-veryshortguide-doc
Documentation for latex-veryshortguide

%package -n texlive-latex-web-companion-doc
Summary:        Documentation for latex-web-companion
Version:        svn29349.0

Provides:       tex-latex-web-companion-doc
AutoReqProv:    No

%description -n texlive-latex-web-companion-doc
Documentation for latex-web-companion

%package -n texlive-latex2e-help-texinfo
Provides:       tex-latex2e-help-texinfo = %{tl_version}
License:        Latex2e
Summary:        Unofficial reference manual covering LaTeX2e
Version:        svn48135
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-latex2e-help-texinfo
The manual is provided as Texinfo source (which was originally
derived from the VMS help file in the DECUS TeX distribution of
1990, with many subsequent changes). This is a collaborative
development, and details of getting involved are to be found on
the package home page. All the other formats in the
distribution are derived from the Texinfo source, as usual.

%package -n texlive-latex2e-help-texinfo-doc
Summary:        Documentation for latex2e-help-texinfo
Version:        svn48135
Provides:       tex-latex2e-help-texinfo-doc
AutoReqProv:    No

%description -n texlive-latex2e-help-texinfo-doc
Documentation for latex2e-help-texinfo

%package -n texlive-latex4wp-doc
Summary:        Documentation for latex4wp
Version:        svn35999.1.0.10

Provides:       tex-latex4wp-doc
AutoReqProv:    No

%description -n texlive-latex4wp-doc
Documentation for latex4wp

%package -n texlive-latexcheat-doc
Summary:        Documentation for latexcheat
Version:        svn15878.1.13

Provides:       tex-latexcheat-doc
AutoReqProv:    No

%description -n texlive-latexcheat-doc
Documentation for latexcheat

%package -n texlive-latexconfig
Provides:       tex-latexconfig = %{tl_version}
License:        LPPL
Summary:        latexconfig package
Version:        svn45777
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(epstopdf-sys.cfg) = %{tl_version}, tex(graphics.cfg) = %{tl_version}
Provides:       tex(hyperref.cfg) = %{tl_version}, tex(lualatex-patch-kernel.tex) = %{tl_version}
Provides:       tex(lualatex-reset-codes.tex) = %{tl_version}
Provides:       tex(lualatexiniconfig.tex) = %{tl_version}
Provides:       tex(lualatexquotejobname.tex) = %{tl_version}

%description -n texlive-latexconfig
latexconfig package

%package -n texlive-latex-fonts
Provides:       tex-latex-fonts = %{tl_version}
License:        LPPL
Summary:        A collection of fonts used in LaTeX distributions
Version:        svn28888.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(icmcsc10.tfm) = %{tl_version}, tex(icmex10.tfm) = %{tl_version}
Provides:       tex(icmmi8.tfm) = %{tl_version}, tex(icmsy8.tfm) = %{tl_version}
Provides:       tex(icmtt8.tfm) = %{tl_version}, tex(ilasy8.tfm) = %{tl_version}
Provides:       tex(ilcmss8.tfm) = %{tl_version}, tex(ilcmssb8.tfm) = %{tl_version}
Provides:       tex(ilcmssi8.tfm) = %{tl_version}, tex(lasy10.tfm) = %{tl_version}
Provides:       tex(lasy5.tfm) = %{tl_version}, tex(lasy6.tfm) = %{tl_version}
Provides:       tex(lasy7.tfm) = %{tl_version}, tex(lasy8.tfm) = %{tl_version}
Provides:       tex(lasy9.tfm) = %{tl_version}, tex(lasyb10.tfm) = %{tl_version}
Provides:       tex(lcircle10.tfm) = %{tl_version}, tex(lcirclew10.tfm) = %{tl_version}
Provides:       tex(lcmss8.tfm) = %{tl_version}, tex(lcmssb8.tfm) = %{tl_version}
Provides:       tex(lcmssi8.tfm) = %{tl_version}, tex(line10.tfm) = %{tl_version}
Provides:       tex(linew10.tfm) = %{tl_version}

%description -n texlive-latex-fonts
This is a collection of fonts for use with standard LaTeX
packages and classes. It includes 'invisible' fonts (for use
with the slides class), line and circle fonts (for use in the
picture environment) and 'LaTeX symbol' fonts. For full support
of a LaTeX installation, some Computer Modern font variants
cmbsy(6-9), cmcsc(8,9), cmex(7-9) and cmmib(5-9) from the
amsfonts distribution, are also necessary. The fonts are
available as Metafont source, and metric (tfm) files are also
provided. Most of the fonts are also available in Adobe Type 1
format, in the amsfonts distribution.

%package -n texlive-latex-fonts-doc
Summary:        Documentation for latex-fonts
Version:        svn28888.0

Provides:       tex-latex-fonts-doc
AutoReqProv:    No

%description -n texlive-latex-fonts-doc
Documentation for latex-fonts

%package -n texlive-lambda
Provides:       tex-lambda = %{tl_version}
License:        LPPL
Summary:        lambda package
Version:        svn45756
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(grlccode.tex)
Provides:       tex(UT1cmr.fd) = %{tl_version}, tex(UT1omlgc.fd) = %{tl_version}
Provides:       tex(elhyph16.tex) = %{tl_version}, tex(grcodes.tex) = %{tl_version}
Provides:       tex(grmhyph.tex) = %{tl_version}, tex(lambda.tex) = %{tl_version}
Provides:       tex(lchcmr.fd) = %{tl_version}, tex(lchenc.def) = %{tl_version}
Provides:       tex(ocherokee.sty) = %{tl_version}, tex(odev.sty) = %{tl_version}
Provides:       tex(ojapan.sty) = %{tl_version}, tex(omarab.cfg) = %{tl_version}
Provides:       tex(omega.sty) = %{tl_version}, tex(omlgc.cfg) = %{tl_version}
Provides:       tex(ot1omarb.fd) = %{tl_version}, tex(ot1omlgc.fd) = %{tl_version}
Provides:       tex(ot1uctt.fd) = %{tl_version}, tex(ut1enc.def) = %{tl_version}
Provides:       tex(language.dat) = %{tl_version}

%description -n texlive-lambda
lambda package

%package -n texlive-leadsheets
Provides:       tex-leadsheets = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting leadsheets and songbooks
Version:        svn45405
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(xparse.sty), tex(translations.sty)
Provides:       tex(leadsheets.library.chordnames.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.chords.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musejazz.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.musicsymbols.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.properties.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.shorthands.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.songs.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.templates.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.translations.code.tex) = %{tl_version}
Provides:       tex(leadsheets.library.transposing.code.tex) = %{tl_version}
Provides:       tex(leadsheets.sty) = %{tl_version}

%description -n texlive-leadsheets
This LaTeX package offers support for typesetting simple
leadsheets of songs, i.e. song lyrics and the corresponding
chords.

%package -n texlive-leadsheets-doc
Summary:        Documentation for leadsheets
Version:        svn45405
Provides:       tex-leadsheets-doc
AutoReqProv:    No

%description -n texlive-leadsheets-doc
Documentation for leadsheets


%package -n texlive-latexcourse-rug-doc
Summary:        Documentation for latexcourse-rug
Version:        svn39026

Provides:       tex-latexcourse-rug-doc
AutoReqProv:    No

%description -n texlive-latexcourse-rug-doc
Documentation for latexcourse-rug

%package -n texlive-latexfileinfo-pkgs
Provides:       tex-latexfileinfo-pkgs = %{tl_version}
License:        LPPL 1.3
Summary:        A comparison of packages showing LaTeX file information
Version:        svn26760.0.22

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-latexfileinfo-pkgs
The package provides an HTML file that lists and compares CTAN
packages that display LaTeX source file information from
\ProvidesClass, \ProvidesFile, and \ProvidesPackage commands in
the LaTeX file. Five packages of the author's, and several
other packages are discussed; revision control systems are
mentioned briefly.

%package -n texlive-latexfileinfo-pkgs-doc
Summary:        Documentation for latexfileinfo-pkgs
Version:        svn26760.0.22

Provides:       tex-latexfileinfo-pkgs-doc
AutoReqProv:    No

%description -n texlive-latexfileinfo-pkgs-doc
Documentation for latexfileinfo-pkgs

%package -n texlive-lshort-english-doc
Summary:        Documentation for lshort-english
Version:        svn37892.5.0.5

Provides:       tex-lshort-english-doc
AutoReqProv:    No

%description -n texlive-lshort-english-doc
Documentation for lshort-english

%package -n texlive-lithuanian
Provides:       tex-lithuanian = %{tl_version}
License:        LPPL
Summary:        Lithuanian language support
Version:        svn46039
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(latin7x.enc) = %{tl_version}, tex(l7x-urwvn.map) = %{tl_version}
Provides:       tex(l7x-uagd.tfm) = %{tl_version}, tex(l7x-uagdo.tfm) = %{tl_version}
Provides:       tex(l7x-uagk.tfm) = %{tl_version}, tex(l7x-uagko.tfm) = %{tl_version}
Provides:       tex(l7x-ubkd.tfm) = %{tl_version}, tex(l7x-ubkdi.tfm) = %{tl_version}
Provides:       tex(l7x-ubkl.tfm) = %{tl_version}, tex(l7x-ubkli.tfm) = %{tl_version}
Provides:       tex(l7x-ucrb.tfm) = %{tl_version}, tex(l7x-ucrbo.tfm) = %{tl_version}
Provides:       tex(l7x-ucrr.tfm) = %{tl_version}, tex(l7x-ucrro.tfm) = %{tl_version}
Provides:       tex(l7x-uhvb.tfm) = %{tl_version}, tex(l7x-uhvbc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvbo.tfm) = %{tl_version}, tex(l7x-uhvboc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvr.tfm) = %{tl_version}, tex(l7x-uhvrc.tfm) = %{tl_version}
Provides:       tex(l7x-uhvro.tfm) = %{tl_version}, tex(l7x-uhvroc.tfm) = %{tl_version}
Provides:       tex(l7x-uncb.tfm) = %{tl_version}, tex(l7x-uncbi.tfm) = %{tl_version}
Provides:       tex(l7x-uncr.tfm) = %{tl_version}, tex(l7x-uncri.tfm) = %{tl_version}
Provides:       tex(l7x-uplb.tfm) = %{tl_version}, tex(l7x-uplbi.tfm) = %{tl_version}
Provides:       tex(l7x-uplr.tfm) = %{tl_version}, tex(l7x-uplri.tfm) = %{tl_version}
Provides:       tex(l7x-utmb.tfm) = %{tl_version}, tex(l7x-utmbi.tfm) = %{tl_version}
Provides:       tex(l7x-utmr.tfm) = %{tl_version}, tex(l7x-utmri.tfm) = %{tl_version}
Provides:       tex(l7x-uzcmi.tfm) = %{tl_version}, tex(cp772.def) = %{tl_version}
Provides:       tex(cp774.def) = %{tl_version}, tex(cp775.def) = %{tl_version}
Provides:       tex(cpKBL.def) = %{tl_version}, tex(cpRIM.def) = %{tl_version}
Provides:       tex(l7xenc.def) = %{tl_version}, tex(l7xenc.sty) = %{tl_version}
Provides:       tex(l7xuag.fd) = %{tl_version}, tex(l7xubk.fd) = %{tl_version}
Provides:       tex(l7xucr.fd) = %{tl_version}, tex(l7xuhv.fd) = %{tl_version}
Provides:       tex(l7xunc.fd) = %{tl_version}, tex(l7xupl.fd) = %{tl_version}
Provides:       tex(l7xutm.fd) = %{tl_version}, tex(l7xuzc.fd) = %{tl_version}
Provides:       tex(latin7.def) = %{tl_version}, tex(lithuanian.ldf) = %{tl_version}
Provides:       tex(lithuanian.sty) = %{tl_version}

%description -n texlive-lithuanian
This language support package provides: Lithuanian language
hyphenation patterns; Lithuanian support for Babel; Lithuanian
mapping and metrics for using the URW base-35 Type 1 fonts;
examples for making Lithuanian fonts with fontinst; and extra
tools for intputenc and fontinst.

%package -n texlive-lithuanian-doc
Summary:        Documentation for lithuanian
Version:        svn46039
Provides:       tex-lithuanian-doc
AutoReqProv:    No

%description -n texlive-lithuanian-doc
Documentation for lithuanian

%package -n texlive-lshort-dutch-doc
Summary:        Documentation for lshort-dutch
Version:        svn15878.1.3

Provides:       tex-lshort-dutch-doc
AutoReqProv:    No

%description -n texlive-lshort-dutch-doc
Documentation for lshort-dutch

%package -n texlive-lshort-finnish-doc
Summary:        Documentation for lshort-finnish
Version:        svn15878.0

Provides:       tex-lshort-finnish-doc
AutoReqProv:    No

%description -n texlive-lshort-finnish-doc
Documentation for lshort-finnish

%package -n texlive-lshort-slovenian-doc
Summary:        Documentation for lshort-slovenian
Version:        svn15878.4.20

Provides:       tex-lshort-slovenian-doc
AutoReqProv:    No

%description -n texlive-lshort-slovenian-doc
Documentation for lshort-slovenian

%package -n texlive-lshort-turkish-doc
Summary:        Documentation for lshort-turkish
Version:        svn15878.4.20

Provides:       tex-lshort-turkish-doc
AutoReqProv:    No

%description -n texlive-lshort-turkish-doc
Documentation for lshort-turkish

%package -n texlive-l2tabu-french-doc
Summary:        Documentation for l2tabu-french
Version:        svn31315.2.3

Provides:       tex-l2tabu-french-doc
AutoReqProv:    No

%description -n texlive-l2tabu-french-doc
Documentation for l2tabu-french

%package -n texlive-lshort-french-doc
Summary:        Documentation for lshort-french
Version:        svn23332.5.01fr_0

Provides:       tex-lshort-french-doc
AutoReqProv:    No

%description -n texlive-lshort-french-doc
Documentation for lshort-french

%package -n texlive-l2picfaq-doc
Summary:        Documentation for l2picfaq
Version:        svn19601.1.50

Provides:       tex-l2picfaq-doc
AutoReqProv:    No

%description -n texlive-l2picfaq-doc
Documentation for l2picfaq

%package -n texlive-l2tabu-doc
Summary:        Documentation for l2tabu
Version:        svn39597

Provides:       tex-l2tabu-doc
AutoReqProv:    No

%description -n texlive-l2tabu-doc
Documentation for l2tabu

%package -n texlive-latex-bib-ex-doc
Summary:        Documentation for latex-bib-ex
Version:        svn25831.0

Provides:       tex-latex-bib-ex-doc
AutoReqProv:    No

%description -n texlive-latex-bib-ex-doc
Documentation for latex-bib-ex

%package -n texlive-latex-referenz-doc
Summary:        Documentation for latex-referenz
Version:        svn36671.2

Provides:       tex-latex-referenz-doc
AutoReqProv:    No

%description -n texlive-latex-referenz-doc
Documentation for latex-referenz

%package -n texlive-latex-tabellen-doc
Summary:        Documentation for latex-tabellen
Version:        svn16979.0

Provides:       tex-latex-tabellen-doc
AutoReqProv:    No

%description -n texlive-latex-tabellen-doc
Documentation for latex-tabellen

%package -n texlive-latexcheat-de-doc
Summary:        Documentation for latexcheat-de
Version:        svn35702.0

Provides:       tex-latexcheat-de-doc
AutoReqProv:    No

%description -n texlive-latexcheat-de-doc
Documentation for latexcheat-de

%package -n texlive-lshort-german-doc
Summary:        Documentation for lshort-german
Version:        svn42434
Provides:       tex-lshort-german-doc
AutoReqProv:    No

%description -n texlive-lshort-german-doc
Documentation for lshort-german

%package -n texlive-lualatex-doc-de-doc
Summary:        Documentation for lualatex-doc-de
Version:        svn30474.1.0

Provides:       tex-lualatex-doc-de-doc
AutoReqProv:    No

%description -n texlive-lualatex-doc-de-doc
Documentation for lualatex-doc-de

%package -n texlive-levy
Provides:       tex-levy = %{tl_version}
License:        GPLv2+
Summary:        Fonts for typesetting classical greek
Version:        svn21750.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(grbld10.tfm) = %{tl_version}, tex(grbld8.tfm) = %{tl_version}
Provides:       tex(grbld9.tfm) = %{tl_version}, tex(grreg10.tfm) = %{tl_version}
Provides:       tex(grreg8.tfm) = %{tl_version}, tex(grreg9.tfm) = %{tl_version}
Provides:       tex(greekmacros.tex) = %{tl_version}, tex(slgreek.sty) = %{tl_version}

%description -n texlive-levy
These fonts are derivatives of Kunth's CM fonts. Macros for use
with Plain TeX are included in the package; for use with LaTeX,
see lgreek (with English documentation) or levy (with German
documentation).

%package -n texlive-levy-doc
Summary:        Documentation for levy
Version:        svn21750.0

Provides:       tex-levy-doc
AutoReqProv:    No

%description -n texlive-levy-doc
Documentation for levy

%package -n texlive-lgreek
Provides:       tex-lgreek = %{tl_version}
License:        GPLv2+
Summary:        LaTeX macros for using Silvio Levy's Greek fonts
Version:        svn21818.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(LGcmr.fd) = %{tl_version}, tex(LGcmtt.fd) = %{tl_version}
Provides:       tex(LGenc.def) = %{tl_version}, tex(lgreek.sty) = %{tl_version}

%description -n texlive-lgreek
A conversion of Silvio Levy's Plain TeX macros for use with
LaTeX.

%package -n texlive-lgreek-doc
Summary:        Documentation for lgreek
Version:        svn21818.0

Provides:       tex-lgreek-doc
AutoReqProv:    No

%description -n texlive-lgreek-doc
Documentation for lgreek

%package -n texlive-l2tabu-italian-doc
Summary:        Documentation for l2tabu-italian
Version:        svn25218.2.3

Provides:       tex-l2tabu-italian-doc
AutoReqProv:    No

%description -n texlive-l2tabu-italian-doc
Documentation for l2tabu-italian

%package -n texlive-latex4wp-it-doc
Summary:        Documentation for latex4wp-it
Version:        svn36000.1.0.10

Provides:       tex-latex4wp-it-doc
AutoReqProv:    No

%description -n texlive-latex4wp-it-doc
Documentation for latex4wp-it

%package -n texlive-layaureo
Provides:       tex-layaureo = %{tl_version}
License:        LPPL
Summary:        A package to improve the A4 page layout
Version:        svn19087.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(calc.sty), tex(keyval.sty)
Provides:       tex(layaureo.sty) = %{tl_version}

%description -n texlive-layaureo
This package produces a wide page layout for documents that use
A4 paper size. Moreover, LayAureo provides both a simple hook
for leaving an empty space which is required if pages are
bundled by a press binding (use option binding=length), and an
option called big which it forces typearea to become maximum.

%package -n texlive-layaureo-doc
Summary:        Documentation for layaureo
Version:        svn19087.0.2

Provides:       tex-layaureo-doc
AutoReqProv:    No

%description -n texlive-layaureo-doc
Documentation for layaureo

%package -n texlive-lshort-italian-doc
Summary:        Documentation for lshort-italian
Version:        svn15878.0

Provides:       tex-lshort-italian-doc
AutoReqProv:    No

%description -n texlive-lshort-italian-doc
Documentation for lshort-italian

%package -n texlive-lshort-japanese-doc
Summary:        Documentation for lshort-japanese
Version:        svn36207.0

Provides:       tex-lshort-japanese-doc
AutoReqProv:    No

%description -n texlive-lshort-japanese-doc
Documentation for lshort-japanese

%package -n texlive-luatexja
Provides:       tex-luatexja = %{tl_version}
License:        BSD
Summary:        Typeset Japanese with Lua(La)TeX
Version:        svn48341
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(l3keys2e.sty), tex(fontspec.sty), tex(expl3.sty), tex(filehook.sty)
Requires:       tex(infwarerr.sty), tex(ltxcmds.sty), tex(xkeyval.sty), tex(luatexja-core.sty)
Requires:       tex(luaotfload.sty), tex(pdftexcmds.sty)
Requires:       tex(atbegshi.sty), tex(everyhook.sty), tex(everysel.sty), tex(footmisc.sty)
Requires:       tex(ifluatex.sty), tex(listings.sty), tex(luatexbase-cctb.sty), tex(stfloats.sty)
Requires:       tex(tascmac.sty), tex(unicode-math.sty), tex(xunicode.sty)
Provides:       tex(luatexja-adjust.sty) = %{tl_version}
Provides:       tex(luatexja-ajmacros.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec-24.sty) = %{tl_version}
Provides:       tex(luatexja-fontspec.sty) = %{tl_version}
Provides:       tex(luatexja-otf.sty) = %{tl_version}, tex(luatexja-preset.sty) = %{tl_version}
Provides:       tex(luatexja-ruby.sty) = %{tl_version}, tex(luatexja-zhfonts.sty) = %{tl_version}
Provides:       tex(lltjext.sty) = %{tl_version}, tex(ltj-base.sty) = %{tl_version}
Provides:       tex(ltj-compat-ptex.sty) = %{tl_version}
Provides:       tex(ltj-latex.sty) = %{tl_version}, tex(ltj-plain.sty) = %{tl_version}
Provides:       tex(ltjarticle.cls) = %{tl_version}, tex(ltjbk10.clo) = %{tl_version}
Provides:       tex(ltjbk11.clo) = %{tl_version}, tex(ltjbk12.clo) = %{tl_version}
Provides:       tex(ltjbook.cls) = %{tl_version}, tex(ltjltxdoc.cls) = %{tl_version}
Provides:       tex(ltjreport.cls) = %{tl_version}, tex(ltjsarticle.cls) = %{tl_version}
Provides:       tex(ltjsbook.cls) = %{tl_version}, tex(ltjsize10.clo) = %{tl_version}
Provides:       tex(ltjsize11.clo) = %{tl_version}, tex(ltjsize12.clo) = %{tl_version}
Provides:       tex(ltjskiyou.cls) = %{tl_version}, tex(ltjspf.cls) = %{tl_version}
Provides:       tex(ltjtarticle.cls) = %{tl_version}, tex(ltjtbk10.clo) = %{tl_version}
Provides:       tex(ltjtbk11.clo) = %{tl_version}, tex(ltjtbk12.clo) = %{tl_version}
Provides:       tex(ltjtbook.cls) = %{tl_version}, tex(ltjtreport.cls) = %{tl_version}
Provides:       tex(ltjtsize10.clo) = %{tl_version}, tex(ltjtsize11.clo) = %{tl_version}
Provides:       tex(ltjtsize12.clo) = %{tl_version}, tex(luatexja-compat.sty) = %{tl_version}
Provides:       tex(luatexja-core.sty) = %{tl_version}, tex(luatexja.sty) = %{tl_version}
Provides:       tex(lltjcore.sty) = %{tl_version}, tex(lltjdefs.sty) = %{tl_version}
Provides:       tex(lltjfont.sty) = %{tl_version}, tex(lltjp-fontspec.sty) = %{tl_version}
Provides:       tex(lltjp-footmisc.sty) = %{tl_version}, tex(lltjp-geometry.sty) = %{tl_version}
Provides:       tex(lltjp-listings.sty) = %{tl_version}, tex(lltjp-stfloats.sty) = %{tl_version}
Provides:       tex(lltjp-tascmac.sty) = %{tl_version}, tex(lltjp-unicode-math.sty) = %{tl_version}
Provides:       tex(lltjp-xunicode.sty) = %{tl_version}

%description -n texlive-luatexja
The package offers support for typesetting Japanese documents
with LuaTeX. Either of the Plain and LaTeX2e formats may be
used with the package.

%package -n texlive-luatexja-doc
Summary:        Documentation for luatexja
Version:        svn48341
Provides:       tex-luatexja-doc
AutoReqProv:    No

%description -n texlive-luatexja-doc
Documentation for luatexja

%package -n texlive-lshort-korean-doc
Summary:        Documentation for lshort-korean
Version:        svn15878.4.17

Provides:       tex-lshort-korean-doc
AutoReqProv:    No

%description -n texlive-lshort-korean-doc
Documentation for lshort-korean

%package -n texlive-lshort-thai-doc
Summary:        Documentation for lshort-thai
Version:        svn15878.1.32

Provides:       tex-lshort-thai-doc
AutoReqProv:    No

%description -n texlive-lshort-thai-doc
Documentation for lshort-thai

%package -n texlive-lshort-vietnamese-doc
Summary:        Documentation for lshort-vietnamese
Version:        svn15878.4.00

Provides:       tex-lshort-vietnamese-doc
AutoReqProv:    No

%description -n texlive-lshort-vietnamese-doc
Documentation for lshort-vietnamese

%package -n texlive-lshort-polish-doc
Summary:        Documentation for lshort-polish
Version:        svn15878.0

Provides:       tex-lshort-polish-doc
AutoReqProv:    No

%description -n texlive-lshort-polish-doc
Documentation for lshort-polish

%package -n texlive-latexcheat-ptbr-doc
Summary:        Documentation for latexcheat-ptbr
Version:        svn15878.1.13

Provides:       tex-latexcheat-ptbr-doc
AutoReqProv:    No

%description -n texlive-latexcheat-ptbr-doc
Documentation for latexcheat-ptbr

%package -n texlive-lshort-portuguese-doc
Summary:        Documentation for lshort-portuguese
Version:        svn22569.5.01.0

Provides:       tex-lshort-portuguese-doc
AutoReqProv:    No

%description -n texlive-lshort-portuguese-doc
Documentation for lshort-portuguese

%package -n texlive-l2tabu-spanish-doc
Summary:        Documentation for l2tabu-spanish
Version:        svn15878.1.1

Provides:       tex-l2tabu-spanish-doc
AutoReqProv:    No

%description -n texlive-l2tabu-spanish-doc
Documentation for l2tabu-spanish

%package -n texlive-latex2e-help-texinfo-spanish
Provides:       tex-latex2e-help-texinfo-spanish = %{tl_version}
License:        LPPL
Summary:        latex2e-help-texinfo-spanish package
Version:        svn48139
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-latex2e-help-texinfo-spanish
latex2e-help-texinfo-spanish package

%package -n texlive-latex2e-help-texinfo-spanish-doc
Summary:        Documentation for latex2e-help-texinfo-spanish
Version:        svn48139
Provides:       tex-latex2e-help-texinfo-spanish-doc
AutoReqProv:    No

%description -n texlive-latex2e-help-texinfo-spanish-doc
Documentation for latex2e-help-texinfo-spanish

%package -n texlive-latexcheat-esmx-doc
Summary:        Documentation for latexcheat-esmx
Version:        svn36866.2.00

Provides:       tex-latexcheat-esmx-doc
AutoReqProv:    No

%description -n texlive-latexcheat-esmx-doc
Documentation for latexcheat-esmx

%package -n texlive-lshort-spanish-doc
Summary:        Documentation for lshort-spanish
Version:        svn35050.0.5

Provides:       tex-lshort-spanish-doc
AutoReqProv:    No

%description -n texlive-lshort-spanish-doc
Documentation for lshort-spanish

%package -n texlive-l3kernel
Provides:       tex-l3kernel = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX3 programming conventions
Version:        svn48022
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphics.sty), tex(doc.sty), tex(array.sty), tex(alphalph.sty)
Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(booktabs.sty), tex(color.sty)
Requires:       tex(colortbl.sty), tex(hologo.sty), tex(enumitem.sty), tex(pifont.sty)
Requires:       tex(textcomp.sty), tex(trace.sty), tex(underscore.sty), tex(csquotes.sty)
Requires:       tex(fancyvrb.sty), tex(verbatim.sty), tex(fontenc.sty), tex(lmodern.sty)
Requires:       tex(hypdoc.sty)
Provides:       tex(expl3-code.tex) = %{tl_version}, tex(expl3-generic.tex) = %{tl_version}
Provides:       tex(expl3.sty) = %{tl_version}, tex(l3basics.sty) = %{tl_version}
Provides:       tex(l3bootstrap.sty) = %{tl_version}, tex(l3box.sty) = %{tl_version}
Provides:       tex(l3candidates.sty) = %{tl_version}, tex(l3clist.sty) = %{tl_version}
Provides:       tex(l3coffins.sty) = %{tl_version}, tex(l3color.sty) = %{tl_version}
Provides:       tex(l3doc.cls) = %{tl_version}, tex(l3docstrip.tex) = %{tl_version}
Provides:       tex(l3dvipdfmx.def) = %{tl_version}, tex(l3dvips.def) = %{tl_version}
Provides:       tex(l3expan.sty) = %{tl_version}, tex(l3file.sty) = %{tl_version}
Provides:       tex(l3fp.sty) = %{tl_version}, tex(l3int.sty) = %{tl_version}
Provides:       tex(l3keys.sty) = %{tl_version}, tex(l3msg.sty) = %{tl_version}
Provides:       tex(l3names.sty) = %{tl_version}, tex(l3pdfmode.def) = %{tl_version}
Provides:       tex(l3prg.sty) = %{tl_version}, tex(l3prop.sty) = %{tl_version}
Provides:       tex(l3quark.sty) = %{tl_version}, tex(l3seq.sty) = %{tl_version}
Provides:       tex(l3skip.sty) = %{tl_version}, tex(l3tl.sty) = %{tl_version}
Provides:       tex(l3token.sty) = %{tl_version}, tex(l3unicode-data.def) = %{tl_version}
Provides:       tex(l3xdvipdfmx.def) = %{tl_version}

%description -n texlive-l3kernel
The l3kernel bundle provides an implementation of the LaTeX3
programmers' interface, as a set of packages that run under
LaTeX 2e. The interface provides the foundation on which the
LaTeX3 kernel and other future code are built: it is an API for
TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX 2e packages. All the
files of the bundle are also available in the project's
Subversion (SVN) repository

%package -n texlive-l3kernel-doc
Summary:        Documentation for l3kernel
Version:        svn48022
Provides:       tex-l3kernel-doc
AutoReqProv:    No

%description -n texlive-l3kernel-doc
Documentation for l3kernel

%package -n texlive-l3packages
Provides:       tex-l3packages = %{tl_version}
License:        LPPL 1.3
Summary:        High-level LaTeX3 concepts
Version:        svn47705
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(amstext.sty), tex(graphicx.sty)
Provides:       tex(l3keys2e.sty) = %{tl_version}, tex(xfrac.sty) = %{tl_version}
Provides:       tex(xparse.sty) = %{tl_version}, tex(xtemplate.sty) = %{tl_version}

%description -n texlive-l3packages
The bundle holds prototype implementations of concepts for a
LaTeX designer interface, to be used with the experimental
LaTeX kernel as programming tools and kernel support. Packages
provided in this release are: l3keys2e, which makes the
facilities of the kernel module l3keys available for use by
LaTeX 2e packages; xfrac, which provides flexible split-level
fractions; xparse, which provides a high-level interface for
declaring document commands; and xtemplate, which provides a
means of defining generic functions using a key-value syntax.
All the files of the bundle are also available in the
Subversion (SVN) repository of the LaTeX3 Project. The bundle
on CTAN is based on a snapshot of the SVN repository; it should
be used with copies of the l3kernel at SVN version 6001 or
later.

%package -n texlive-l3packages-doc
Summary:        Documentation for l3packages
Version:        svn47705
Provides:       tex-l3packages-doc
AutoReqProv:    No

%description -n texlive-l3packages-doc
Documentation for l3packages

%package -n texlive-l3experimental
Provides:       tex-l3experimental = %{tl_version}
License:        LPPL 1.3
Summary:        Experimental LaTeX3 concepts
Version:        svn47705
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3tl-analysis.sty), tex(xparse.sty)
Provides:       tex(l3sort.sty) = %{tl_version}, tex(l3flag.sty) = %{tl_version}
Provides:       tex(l3regex-trace.sty) = %{tl_version}, tex(l3regex.sty) = %{tl_version}
Provides:       tex(l3str-convert.sty) = %{tl_version}, tex(l3str-enc-iso88591.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885910.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885911.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885913.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885914.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885915.def) = %{tl_version}
Provides:       tex(l3str-enc-iso885916.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88592.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88593.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88594.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88595.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88596.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88597.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88598.def) = %{tl_version}
Provides:       tex(l3str-enc-iso88599.def) = %{tl_version}
Provides:       tex(l3str-enc-utf16.def) = %{tl_version}
Provides:       tex(l3str-enc-utf32.def) = %{tl_version}
Provides:       tex(l3str-enc-utf8.def) = %{tl_version}, tex(l3str-esc-hex.def) = %{tl_version}
Provides:       tex(l3str-esc-name.def) = %{tl_version}, tex(l3str-esc-string.def) = %{tl_version}
Provides:       tex(l3str-esc-url.def) = %{tl_version}, tex(l3str-format.sty) = %{tl_version}
Provides:       tex(l3str.sty) = %{tl_version}, tex(l3tl-analysis.sty) = %{tl_version}
Provides:       tex(l3tl-build.sty) = %{tl_version}, tex(xcoffins.sty) = %{tl_version}
Provides:       tex(l3galley.sty) = %{tl_version}, tex(xgalley.sty) = %{tl_version}

%description -n texlive-l3experimental
The l3experimental packages are a collection of experimental
implementations for aspects of the LaTeX3 kernel, dealing with
higher-level ideas such as the Designer Interface. Some of them
work as stand alone packages, providing new functionality, and
can be used on top of LaTeX2e with no changes to the existing
kernel. The present release includes: xgalley, which controls
boxes receiving text for typesetting. l3regex: kernel support
for regular expression search and replace operations; l3sort:
kernel support for sorting sequences, token lists or comma-
lists, according to user-specified comparison criteria; l3str:
kernel support for string manipulation; l3tl-build: kernel
support for token list building; l3tl_analysis: kernel support
for token list analysis; and xcoffins, which allows the
alignment of boxes using a series of 'handle' positions,
supplementing the simple TeX reference point. All the files of
the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository.

%package -n texlive-l3experimental-doc
Summary:        Documentation for l3experimental
Version:        svn47705
Provides:       tex-l3experimental-doc
AutoReqProv:    No

%description -n texlive-l3experimental-doc
Documentation for l3experimental

%package -n texlive-lineno
Provides:       tex-lineno = %{tl_version}
License:        LPPL
Summary:        Line numbers on paragraphs
Version:        svn21442.4.41

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty), tex(ltabptch.sty), tex(finstrut.sty)
Provides:       tex(ednmath0.sty) = %{tl_version}, tex(edtable.sty) = %{tl_version}
Provides:       tex(fnlineno.sty) = %{tl_version}, tex(lineno.sty) = %{tl_version}
Provides:       tex(vplref.sty) = %{tl_version}

%description -n texlive-lineno
Adds line numbers to selected paragraphs with reference
possible through the LaTeX \ref and \pageref cross reference
mechanism. Line numbering may be extended to footnote lines,
using the fnlineno package.

%package -n texlive-lineno-doc
Summary:        Documentation for lineno
Version:        svn21442.4.41

Provides:       tex-lineno-doc
AutoReqProv:    No

%description -n texlive-lineno-doc
Documentation for lineno

%package -n texlive-listings
Provides:       tex-listings = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset source code listings using LaTeX
Version:        svn37534.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(textcomp.sty), tex(fancyvrb.sty), tex(hyperref.sty)
Requires:       tex(color.sty), tex(algorithmic.sty), tex(nameref.sty), tex(url.sty)
Provides:       tex(listings.cfg) = %{tl_version}, tex(listings.sty) = %{tl_version}
Provides:       tex(lstdoc.sty) = %{tl_version}, tex(lstlang1.sty) = %{tl_version}
Provides:       tex(lstlang2.sty) = %{tl_version}, tex(lstlang3.sty) = %{tl_version}
Provides:       tex(lstmisc.sty) = %{tl_version}

%description -n texlive-listings
The package enables the user to typeset programs (programming
code) within LaTeX; the source code is read directly by TeX--no
front-end processor is needed. Keywords, comments and strings
can be typeset using different styles (default is bold for
keywords, italic for comments and no special style for
strings). Support for hyperref is provided. To use,
\usepackage{listings}, identify the language of the object to
typeset, using a construct like: \lstset{language=Python}, then
use environment lstlisting for inline code. External files may
be formatted using \lstinputlisting to process a given file in
the form appropriate for the current language. Short (in-line)
listings are also available, using either \lstinline|...| or
|...| (after defining the | token with the \lstMakeShortInline
command).

%package -n texlive-listings-doc
Summary:        Documentation for listings
Version:        svn37534.1.6

Provides:       tex-listings-doc
AutoReqProv:    No

%description -n texlive-listings-doc
Documentation for listings

%package -n texlive-lapdf
Provides:       tex-lapdf = %{tl_version}
License:        GPL+
Summary:        PDF drawing directly in TeX documents
Version:        svn23806.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(lapdf.sty) = %{tl_version}

%description -n texlive-lapdf
The package provides the means to use PDF drawing primitives to
produce high quality, colored graphics. It uses Bezier curves
(integral and rational) from degree one to seven, allows TeX
typesetting in the graphic, offers most of the standard math
functions, allows plotting normal, parametric and polar
functions. The package has linear, logx, logy, logxy and polar
grids with many specs; it can rotate, clip and do many nice
things easily it has two looping commands for programming and
many instructive example files. The package requires pdfTeX but
otherwise only depends on the calc package.

%package -n texlive-lapdf-doc
Summary:        Documentation for lapdf
Version:        svn23806.1.1

Provides:       tex-lapdf-doc
AutoReqProv:    No

%description -n texlive-lapdf-doc
Documentation for lapdf

%package -n texlive-latex-make
Provides:       tex-latex-make = %{tl_version}
License:        GPL+
Summary:        Easy compiling of complex (and simple) LaTeX documents
Version:        svn47869
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(graphicx.sty), tex(color.sty), tex(epstopdf.sty)
Requires:       tex(ae.sty), tex(aeguill.sty), tex(ifthen.sty), tex(ifxetex.sty)
Provides:       tex(figlatex.cfg) = %{tl_version}, tex(figlatex.sty) = %{tl_version}
Provides:       tex(pdfswitch.sty) = %{tl_version}, tex(texdepends.sty) = %{tl_version}
Provides:       tex(texgraphicx.sty) = %{tl_version}

%description -n texlive-latex-make
This package provides several tools that aim to simplify the
compilation of LaTeX documents: LaTeX.mk: a Makefile snippet to
help compiling LaTeX documents in DVI, PDF, PS, ... format.
Dependencies are automatically tracked: one should be able to
compile documents with a one-line Makefile containing 'include
LaTeX.mk'. Complex documents (with multiple bibliographies,
indexes, glossaries, ...) should be correctly managed.
figlatex.sty: a LaTeX package to easily insert xfig figures
(with \includegraphics{file.fig}). It can interact with
LaTeX.mk so that the latter automatically invokes transfig if
needed. And various helper tools for LaTeX.mk This package
requires GNUmake (>= 3.81).

%package -n texlive-latex-make-doc
Summary:        Documentation for latex-make
Version:        svn47869
Provides:       tex-latex-make-doc
AutoReqProv:    No

%description -n texlive-latex-make-doc
Documentation for latex-make

%package -n texlive-lpic
Provides:       tex-lpic = %{tl_version}
License:        LPPL 1.3
Summary:        Put LaTeX material over included graphics
Version:        svn20843.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(epsfig.sty), tex(rotating.sty), tex(calc.sty), tex(ifthen.sty)
Requires:       tex(color.sty)
Provides:       tex(lpic.sty) = %{tl_version}

%description -n texlive-lpic
The package defines a convenient interface to put any LaTeX
material on top of included graphics. The LaTeX material may
also be rotated and typeset on top of a white box overshadowing
the graphics. The coordinates of the LaTeX boxes are given
relative to the original, unscaled graphics; when the graphics
is rescaled, the LaTeX annotations stay at their right places
(unless you do something extreme). In a draft mode, the package
enables you to draw a coordinate grid over the picture for easy
adjustment of positions of the annotations.

%package -n texlive-lpic-doc
Summary:        Documentation for lpic
Version:        svn20843.0.8

Provides:       tex-lpic-doc
AutoReqProv:    No

%description -n texlive-lpic-doc
Documentation for lpic

%package -n texlive-labbook
Provides:       tex-labbook = %{tl_version}
License:        LPPL
Summary:        Typeset laboratory journals
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makeidx.sty)
Provides:       tex(labbook.cls) = %{tl_version}

%description -n texlive-labbook
This class is designed to typeset laboratory journals that
contain chronologically ordered records about experiments. From
the sectioning commands, an experiment index is generated. The
class is based on the KOMA-Script class scrbook.cls. There can
be several index entries for one experiment.

%package -n texlive-labbook-doc
Summary:        Documentation for labbook
Version:        svn15878.0

Provides:       tex-labbook-doc
AutoReqProv:    No

%description -n texlive-labbook-doc
Documentation for labbook

%package -n texlive-labels
Provides:       tex-labels = %{tl_version}
License:        LPPL 1.2
Summary:        Print sheets of sticky labels
Version:        svn15878.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(labels.sty) = %{tl_version}, tex(olabels.sty) = %{tl_version}

%description -n texlive-labels
A LaTeX package to print a regular grid of ragged-right labels
on a page, suitable for sheets of labels which can be fed
through a printer. Macros are provided to allow easy input of
names and addresses in a form free of TeX markup. Equally
useful is a feature for making multiple copies of a single
label, e.g., return address stickers to go with the labels.
Rows, columns, borders can all be specified to match the label
sheet being used.

%package -n texlive-labels-doc
Summary:        Documentation for labels
Version:        svn15878.13

Provides:       tex-labels-doc
AutoReqProv:    No

%description -n texlive-labels-doc
Documentation for labels

%package -n texlive-lastpackage
Provides:       tex-lastpackage = %{tl_version}
License:        LPPL 1.3
Summary:        Indicates the last loaded package
Version:        svn34481.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lastpackage.sty) = %{tl_version}

%description -n texlive-lastpackage
This package may be used to define the last point where some
code shall be executed. Its provides a package name for use in
package-placing commands from the author's templatetools. Usage
examples are provided in the documentation.

%package -n texlive-lastpackage-doc
Summary:        Documentation for lastpackage
Version:        svn34481.0.1

Provides:       tex-lastpackage-doc
AutoReqProv:    No

%description -n texlive-lastpackage-doc
Documentation for lastpackage

%package -n texlive-lastpage
Provides:       tex-lastpage = %{tl_version}
License:        LPPL 1.3
Summary:        Reference last page for Page N of M type footers
Version:        svn36680.1.2m

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lastpage.sty) = %{tl_version}, tex(lastpage209.sty) = %{tl_version}

%description -n texlive-lastpage
Reference the number of pages in your LaTeX document through
the introduction of a new label which can be referenced like
\pageref{LastPage} to give a reference to the last page of a
document. It is particularly useful in the page footer that
says: Page N of M.

%package -n texlive-lastpage-doc
Summary:        Documentation for lastpage
Version:        svn36680.1.2m

Provides:       tex-lastpage-doc
AutoReqProv:    No

%description -n texlive-lastpage-doc
Documentation for lastpage

%package -n texlive-latexdemo
Provides:       tex-latexdemo = %{tl_version}
License:        LPPL 1.3
Summary:        Demonstrate LaTeX code with its resulting output
Version:        svn34481.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(doctools.sty), tex(listings.sty), tex(xspace.sty), tex(etoolbox.sty)
Requires:       tex(filecontents.sty), tex(mdframed.sty)
Requires:       tex(framed.sty), tex(xcolor.sty), tex(kvoptions-patch.sty), tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Provides:       tex(latexdemo.sty) = %{tl_version}

%description -n texlive-latexdemo
The package provides configurable tools to print out LaTeX code
and the resulting output in the same document. It also supports
printing the result inside a conditional sequence; thus one may
suppress printing if the code would not compile.

%package -n texlive-latexdemo-doc
Summary:        Documentation for latexdemo
Version:        svn34481.0.1

Provides:       tex-latexdemo-doc
AutoReqProv:    No

%description -n texlive-latexdemo-doc
Documentation for latexdemo

%package -n texlive-layouts
Provides:       tex-layouts = %{tl_version}
License:        LPPL 1.3
Summary:        Display various elements of a document's layout
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(layouts.sty) = %{tl_version}

%description -n texlive-layouts
Display information about a document, including: text
positioning on a page; disposition of floats; layout of
paragraphs, lists, footnotes, table of contents, and sectional
headings; font boxes. Facilities are provided for a document
designer to experiment with the layout parameters.

%package -n texlive-layouts-doc
Summary:        Documentation for layouts
Version:        svn42428
Provides:       tex-layouts-doc
AutoReqProv:    No

%description -n texlive-layouts-doc
Documentation for layouts

%package -n texlive-lazylist
Provides:       tex-lazylist = %{tl_version}
License:        LPPL 1.2
Summary:        Lists in TeX's "mouth"
Version:        svn17691.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lazylist.sty) = %{tl_version}

%description -n texlive-lazylist
The package was developed to provide flexible lists, whose
ordering can be altered on the fly. The implementation involves
a pile of lambda-calculus and list-handling macros of an
incredibly obtuse nature. The TUGboat paper serves as a manual
for the macros. Having said all of which, confidence is
enhanced by the knowledge that the TeX code was formally
verified.

%package -n texlive-lazylist-doc
Summary:        Documentation for lazylist
Version:        svn17691.1.0a

Provides:       tex-lazylist-doc
AutoReqProv:    No

%description -n texlive-lazylist-doc
Documentation for lazylist

%package -n texlive-lcd
Provides:       tex-lcd = %{tl_version}
License:        LPPL
Summary:        Alphanumerical LCD-style displays
Version:        svn16549.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lcd.sty) = %{tl_version}

%description -n texlive-lcd
A LaTeX package that will display text as on an (early) LCD
display (the output is very visibly pixellated). Assumes 8-bit
input in its internal verbatim-style environment.

%package -n texlive-lcd-doc
Summary:        Documentation for lcd
Version:        svn16549.0.3

Provides:       tex-lcd-doc
AutoReqProv:    No

%description -n texlive-lcd-doc
Documentation for lcd

%package -n texlive-lcg
Provides:       tex-lcg = %{tl_version}
License:        LPPL
Summary:        Generate random integers
Version:        svn31474.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(lcg.sty) = %{tl_version}

%description -n texlive-lcg
The lcg package generates random numbers (integers) via a
linear congruential generator (Schrage's method). The random
numbers are written to a counter. The keyval package is used
for the user to provide values for the range and a seed, and
for the name of the counter to be used.

%package -n texlive-lcg-doc
Summary:        Documentation for lcg
Version:        svn31474.1.3

Provides:       tex-lcg-doc
AutoReqProv:    No

%description -n texlive-lcg-doc
Documentation for lcg

%package -n texlive-leading
Provides:       tex-leading = %{tl_version}
License:        LPPL
Summary:        Define leading with a length
Version:        svn15878.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(leading.sty) = %{tl_version}

%description -n texlive-leading
The package defines a command \leading, whose argument is a
<length> that specifies the nominal distance between
consecutive baselines of typeset text. The command replaces the
rather more difficult LaTeX command \linespread{<ratio>}, where
the leading is specified by reference to the font size.

%package -n texlive-leading-doc
Summary:        Documentation for leading
Version:        svn15878.0.3

Provides:       tex-leading-doc
AutoReqProv:    No

%description -n texlive-leading-doc
Documentation for leading

%package -n texlive-leaflet
Provides:       tex-leaflet = %{tl_version}
License:        LPPL
Summary:        Create small handouts (flyers)
Version:        svn43523
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etex.sty), tex(everyshi.sty), tex(calc.sty), tex(graphicx.sty)
Requires:       tex(pifont.sty)
Provides:       tex(leaflet.cls) = %{tl_version}

%description -n texlive-leaflet
A document class to create small hand-outs (flyers) that fit on
a single sheet of paper which is then folded twice. Pages are
rearranged by LaTeX so that they print correctly on a single
sheet -- no external script is necessary. (Works with
PostScript and PDF.) This is a complete reimplementation with
permission of the original author Jurgen Schlegelmilch.

%package -n texlive-leaflet-doc
Summary:        Documentation for leaflet
Version:        svn43523
Provides:       tex-leaflet-doc
AutoReqProv:    No

%description -n texlive-leaflet-doc
Documentation for leaflet

%package -n texlive-leftidx
Provides:       tex-leftidx = %{tl_version}
License:        LPPL
Summary:        Left and right subscripts and superscripts in math mode
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(leftidx.sty) = %{tl_version}

%description -n texlive-leftidx
Left and right subscripts and superscripts are automatically
raised for better fitting to the symbol they belong to.

%package -n texlive-leftidx-doc
Summary:        Documentation for leftidx
Version:        svn15878.0

Provides:       tex-leftidx-doc
AutoReqProv:    No

%description -n texlive-leftidx-doc
Documentation for leftidx

%package -n texlive-lengthconvert
Provides:       tex-lengthconvert = %{tl_version}
License:        LPPL 1.3
Summary:        Express lengths in arbitrary units
Version:        svn30867.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty)
Provides:       tex(lengthconvert.sty) = %{tl_version}

%description -n texlive-lengthconvert
The package provides a command to convert a length to any of a
large selection of units. The package relies on the LaTeX 3
programming environment.

%package -n texlive-lengthconvert-doc
Summary:        Documentation for lengthconvert
Version:        svn30867.1.0a

Provides:       tex-lengthconvert-doc
AutoReqProv:    No

%description -n texlive-lengthconvert-doc
Documentation for lengthconvert

%package -n texlive-lettre
Provides:       tex-lettre = %{tl_version}
License:        LPPL 1.3
Summary:        Letters and faxes in French
Version:        svn44950
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(lettre.cls) = %{tl_version}

%description -n texlive-lettre
Developed from the ancestor of the standard letter class, at
the Observatoire de Geneve.

%package -n texlive-lettre-doc
Summary:        Documentation for lettre
Version:        svn44950
Provides:       tex-lettre-doc
AutoReqProv:    No

%description -n texlive-lettre-doc
Documentation for lettre

%package -n texlive-lettrine
Provides:       tex-lettrine = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset dropped capitals
Version:        svn48321
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(lettrine.cfg) = %{tl_version}, tex(lettrine.sty) = %{tl_version}

%description -n texlive-lettrine
The lettrine package supports various dropped capitals styles,
typically those described in the French typographic books. In
particular, it has facilities for the paragraph text's left
edge to follow the outline of capitals that have a regular
shape (such as "A" and "V").

%package -n texlive-lettrine-doc
Summary:        Documentation for lettrine
Version:        svn48321
Provides:       tex-lettrine-doc
AutoReqProv:    No

%description -n texlive-lettrine-doc
Documentation for lettrine

%package -n texlive-lewis
Provides:       tex-lewis = %{tl_version}
License:        Public Domain
Summary:        Draw Lewis structures
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lewis.sty) = %{tl_version}

%description -n texlive-lewis
The package provides rudimentary support for drawing Lewis
Structures. Support is limited to elements that support the
octet rule.

%package -n texlive-lewis-doc
Summary:        Documentation for lewis
Version:        svn15878.0.1

Provides:       tex-lewis-doc
AutoReqProv:    No

%description -n texlive-lewis-doc
Documentation for lewis

%package -n texlive-lhelp
Provides:       tex-lhelp = %{tl_version}
License:        GPL+
Summary:        Miscellaneous helper packages
Version:        svn23638.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty), tex(color.sty)
Provides:       tex(lhelp.sty) = %{tl_version}

%description -n texlive-lhelp
This package defines macros which are useful for many
documents. It is a large collection of simple 'little helpers'
which do not really warrant a separate package on their own.
Included are, among other things, definitions of common units
with preceeding thinspaces, framed boxes where both width and
height can be specified, starting new odd or even pages, draft
markers, notes, conditional includes, including EPS files, and
versions of enumerate and itemize which allow the horizontal
and vertical spacing to be changed.

%package -n texlive-lhelp-doc
Summary:        Documentation for lhelp
Version:        svn23638.2.0

Provides:       tex-lhelp-doc
AutoReqProv:    No

%description -n texlive-lhelp-doc
Documentation for lhelp

%package -n texlive-libgreek
Provides:       tex-libgreek = %{tl_version}
License:        LPPL 1.3
Summary:        Use Libertine or Biolinum Greek glyphs in mathematics
Version:        svn27789.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(libgreek.sty) = %{tl_version}

%description -n texlive-libgreek
The package is for LaTeX users who wish to use the Libertine or
Biolinum font for the Greek letters in math mode. It is not
necessary to load the libertine package itself, but of course
the Linux-Libertine/Biolinum fonts and LaTeX support files must
have been installed.

%package -n texlive-libgreek-doc
Summary:        Documentation for libgreek
Version:        svn27789.1.0

Provides:       tex-libgreek-doc
AutoReqProv:    No

%description -n texlive-libgreek-doc
Documentation for libgreek

%package -n texlive-limap
Provides:       tex-limap = %{tl_version}
License:        LPPL
Summary:        Typeset maps and blocks according to the Information Mapping method
Version:        svn44863
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(longtable.sty), tex(booktabs.sty), tex(fancyhdr.sty)
Provides:       tex(limap.cls) = %{tl_version}, tex(limap.sty) = %{tl_version}

%description -n texlive-limap
The Information Mapping method provides a methodology for
structuring and presenting information. It claims to be useful
for readers who are more concerned about finding the right
information than reading the document as a whole. Thus short,
highly structured, and context free pieces of information are
used. A LaTeX style and a LaTeX class are provided. The style
contains definitions to typeset maps and blocks according to
the Information Mapping method. The class provides all
definitions to typeset a whole document.

%package -n texlive-linegoal
Provides:       tex-linegoal = %{tl_version}
License:        LPPL 1.3
Summary:        A "dimen" that returns the space left on the line
Version:        svn21523.2.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(zref.sty), tex(zref-savepos.sty)
Provides:       tex(linegoal.sty) = %{tl_version}

%description -n texlive-linegoal
The linegoal package provides a macro \linegoal to be used with
\setlength: \setlength<some dimen>\linegoal will set <some
dimen> to the horizontal length of the remainder of the line.
This is achieved using the \pdfsavepos primitive of pdftex,
through the zref-savepos package. Example: Some text:
\begin{tabularx}\linegoal{|l|X|} \hline one & two \\ three &
four \\\hline \end{tabularx} will position the table after the
initial text, and make the table fill the rest of the line.

%package -n texlive-linegoal-doc
Summary:        Documentation for linegoal
Version:        svn21523.2.9

Provides:       tex-linegoal-doc
AutoReqProv:    No

%description -n texlive-linegoal-doc
Documentation for linegoal

%package -n texlive-lipsum
Provides:       tex-lipsum = %{tl_version}
License:        LPPL
Summary:        Easy access to the Lorem Ipsum dummy text
Version:        svn34800.v1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lipsum.sty) = %{tl_version}

%description -n texlive-lipsum
This package gives you easy access to the Lorem Ipsum dummy
text; an option is available to separate the paragraphs of the
dummy text into TeX-paragraphs. All the paragraphs are taken
with permission from http://lipsum.com/.

%package -n texlive-lipsum-doc
Summary:        Documentation for lipsum
Version:        svn34800.v1.3

Provides:       tex-lipsum-doc
AutoReqProv:    No

%description -n texlive-lipsum-doc
Documentation for lipsum

%package -n texlive-lisp-on-tex
Provides:       tex-lisp-on-tex = %{tl_version}
License:        BSD
Summary:        Execute LISP code in a LaTeX document
Version:        svn38722

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lisp-arith.sty) = %{tl_version}, tex(lisp-gc.sty) = %{tl_version}
Provides:       tex(lisp-latexutil.sty) = %{tl_version}, tex(lisp-mod-fpnum.sty) = %{tl_version}
Provides:       tex(lisp-mod-l3regex.sty) = %{tl_version}
Provides:       tex(lisp-on-tex.sty) = %{tl_version}, tex(lisp-prim.sty) = %{tl_version}
Provides:       tex(lisp-read.sty) = %{tl_version}, tex(lisp-simple-alloc.sty) = %{tl_version}
Provides:       tex(lisp-string.sty) = %{tl_version}, tex(lisp-util.sty) = %{tl_version}

%description -n texlive-lisp-on-tex
The package provides a LISP interpreter written using TeX
macros; it is provided as a LaTeX package. The interpreter
static scoping, dynamic typing, and eager evaluation.

%package -n texlive-lisp-on-tex-doc
Summary:        Documentation for lisp-on-tex
Version:        svn38722

Provides:       tex-lisp-on-tex-doc
AutoReqProv:    No

%description -n texlive-lisp-on-tex-doc
Documentation for lisp-on-tex

%package -n texlive-listing
Provides:       tex-listing = %{tl_version}
License:        LPPL
Summary:        Produce formatted program listings
Version:        svn17373.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(listing.sty) = %{tl_version}

%description -n texlive-listing
The listing environment is provided and is similar to figure
and table, although it is not a floating environment. Includes
support for \caption, \label, \ref, and introduces
\listoflistings, \listingname, \listlistingname. It produces a
.lol file. It does not change \@makecaption (unless the option
bigcaptions is used), so packages that change the layout of
\caption still work.

%package -n texlive-listing-doc
Summary:        Documentation for listing
Version:        svn17373.1.2

Provides:       tex-listing-doc
AutoReqProv:    No

%description -n texlive-listing-doc
Documentation for listing

%package -n texlive-listlbls
Provides:       tex-listlbls = %{tl_version}
License:        LPPL 1.3
Summary:        Creates a list of all labels used throughout a document
Version:        svn34893.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(translations.sty)
Provides:       tex(listlbls.sty) = %{tl_version}

%description -n texlive-listlbls
The package aims to help a LaTeX author to keep track of all
defined labels by typesetting a complete list of labels
wherever the author requests it. (Of course, the user may need
to have additional LaTeX runs to get the references right. )
This package is based on an answer David Carlisle gave on
TeX/Stackexchange in the thread 'List of all labels with
hyperlinks'.

%package -n texlive-listlbls-doc
Summary:        Documentation for listlbls
Version:        svn34893.1.03

Provides:       tex-listlbls-doc
AutoReqProv:    No

%description -n texlive-listlbls-doc
Documentation for listlbls

%package -n texlive-listliketab
Provides:       tex-listliketab = %{tl_version}
License:        LPPL
Summary:        Typeset lists as tables
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(array.sty)
Provides:       tex(listliketab.sty) = %{tl_version}

%description -n texlive-listliketab
The listliketab package helps the user make list-like tabulars,
i.e., a tabular that is indistinguishable from an itemize or
enumerate environment. The advantage of using a tabular is that
the user can add additional columns to each entry in the list.

%package -n texlive-listliketab-doc
Summary:        Documentation for listliketab
Version:        svn15878.0

Provides:       tex-listliketab-doc
AutoReqProv:    No

%description -n texlive-listliketab-doc
Documentation for listliketab

%package -n texlive-listofsymbols
Provides:       tex-listofsymbols = %{tl_version}
License:        LPPL
Summary:        Create and manipulate lists of symbols
Version:        svn16134.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(nomencl.sty), tex(xspace.sty)
Provides:       tex(listofsymbols.sty) = %{tl_version}

%description -n texlive-listofsymbols
Listofsymbols provides commands to automatically create a list
of symbols (also called notation or nomenclature), and to
handle symbols logically, i.e. define a macro that is expanded
to the desired output and use the macro in the text rather than
`hardcoding' the output into the text. This helps to ensure
consistency throughout the text, especially if there is a
chance that symbols will be changed at some stage. The package
is more or less a combination of what the packages nomencl and
formula do. The concept of creating the list of symbols,
though, is different from the way nomencl.sty does it.

%package -n texlive-listofsymbols-doc
Summary:        Documentation for listofsymbols
Version:        svn16134.0.2

Provides:       tex-listofsymbols-doc
AutoReqProv:    No

%description -n texlive-listofsymbols-doc
Documentation for listofsymbols

%package -n texlive-lkproof
Provides:       tex-lkproof = %{tl_version}
License:        GPL+
Summary:        LK Proof figure macros
Version:        svn20021.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(proof.sty) = %{tl_version}

%description -n texlive-lkproof
The package defines a pair of commands \infer and \deduce, that
are used in constructing LK proof diagrams.

%package -n texlive-lkproof-doc
Summary:        Documentation for lkproof
Version:        svn20021.3.1

Provides:       tex-lkproof-doc
AutoReqProv:    No

%description -n texlive-lkproof-doc
Documentation for lkproof

%package -n texlive-lmake
Provides:       tex-lmake = %{tl_version}
License:        LPPL 1.2
Summary:        Process lists to do repetitive actions
Version:        svn25552.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lmake.sty) = %{tl_version}

%description -n texlive-lmake
The package provides commands to simplify processing of
sequential list-like structures, such as making a series of
'similar' commands from a list of names.

%package -n texlive-lmake-doc
Summary:        Documentation for lmake
Version:        svn25552.1.0

Provides:       tex-lmake-doc
AutoReqProv:    No

%description -n texlive-lmake-doc
Documentation for lmake

%package -n texlive-locality
Provides:       tex-locality = %{tl_version}
License:        LPPL 1.3
Summary:        Various macros for keeping things local
Version:        svn20422.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty)
Provides:       tex(locality.sty) = %{tl_version}

%description -n texlive-locality
A toolbox of macros designed to allow the LaTeX programmer to
work around some of the restrictions of the TeX grouping
mechanisms. The present release offers a preliminary view of
the package; not all of its facilities are working optimally

%package -n texlive-locality-doc
Summary:        Documentation for locality
Version:        svn20422.0.2

Provides:       tex-locality-doc
AutoReqProv:    No

%description -n texlive-locality-doc
Documentation for locality

%package -n texlive-localloc
Provides:       tex-localloc = %{tl_version}
License:        Bibtex
Summary:        Macros for localizing TeX register allocations
Version:        svn21934.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(localloc.sty) = %{tl_version}

%description -n texlive-localloc
This package approaches the problem of the shortage of
registers, by providing a mechanism for local allocation. The
package works with Plain TeX, LaTeX and LaTeX 2.09.

%package -n texlive-localloc-doc
Summary:        Documentation for localloc
Version:        svn21934.0

Provides:       tex-localloc-doc
AutoReqProv:    No

%description -n texlive-localloc-doc
Documentation for localloc

%package -n texlive-logbox
Provides:       tex-logbox = %{tl_version}
License:        LPPL 1.3
Summary:        e-TeX showbox facilities for exploration purposes
Version:        svn24499.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(logbox.sty) = %{tl_version}

%description -n texlive-logbox
The command \logbox does \showbox without stopping the
compilation. The package's main command is \viewbox*: the box
is typeset (copied) with its dimensions, and its contents are
logged in the .log file.

%package -n texlive-logbox-doc
Summary:        Documentation for logbox
Version:        svn24499.1.0

Provides:       tex-logbox-doc
AutoReqProv:    No

%description -n texlive-logbox-doc
Documentation for logbox

%package -n texlive-logical-markup-utils
Provides:       tex-logical-markup-utils = %{tl_version}
License:        GPLv3+
Summary:        Packages for language-dependent inline quotes and dashes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(onedash.sty) = %{tl_version}, tex(quoted.sty) = %{tl_version}

%description -n texlive-logical-markup-utils
The bundle contains two packages: quoted, for inserting
quotation marks; and onedash, for inserting dashes. Each
package takes a language name as an option; accepted language
options are american, british, german and polish.

%package -n texlive-logical-markup-utils-doc
Summary:        Documentation for logical-markup-utils
Version:        svn15878.0

Provides:       tex-logical-markup-utils-doc
AutoReqProv:    No

%description -n texlive-logical-markup-utils-doc
Documentation for logical-markup-utils

%package -n texlive-logpap
Provides:       tex-logpap = %{tl_version}
License:        LPPL
Summary:        Generate logarithmic graph paper with LaTeX
Version:        svn15878.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(color.sty)
Provides:       tex(logpap.sty) = %{tl_version}

%description -n texlive-logpap
The logpap package provides four macros for drawing logarithmic-
logarithmic, logarithmic-linear, linear-logarithmic and
(because it was easy to implement) linear-linear graph paper
with LaTeX.

%package -n texlive-logpap-doc
Summary:        Documentation for logpap
Version:        svn15878.0.6

Provides:       tex-logpap-doc
AutoReqProv:    No

%description -n texlive-logpap-doc
Documentation for logpap

%package -n texlive-longfigure
Provides:       tex-longfigure = %{tl_version}
License:        LPPL 1.3
Summary:        Provides a figure-like environment that break over pages
Version:        svn34302.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(tocloft.sty)
Provides:       tex(longfigure.sty) = %{tl_version}

%description -n texlive-longfigure
The longfigure package uses and relabels components of the well-
known longtable package, written by David Carlisle, to provide
a table-like environment that can display a stream of figures
as a single figure that can break across pages.

%package -n texlive-longfigure-doc
Summary:        Documentation for longfigure
Version:        svn34302.1.0

Provides:       tex-longfigure-doc
AutoReqProv:    No

%description -n texlive-longfigure-doc
Documentation for longfigure

%package -n texlive-longnamefilelist
Provides:       tex-longnamefilelist = %{tl_version}
License:        LPPL 1.3
Summary:        Tidy \listfiles with long file names
Version:        svn27889.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(myfilist.sty)
Provides:       tex(longnamefilelist.sty) = %{tl_version}

%description -n texlive-longnamefilelist
The package equips LaTeX's \listfiles command with an optional
argument for the number of characters in the longest base
filename. This way you get a neatly aligned file list even when
it contains files whose base names have more than 8 characters.
The package can be combined with the myfilist package as
explained in the documentation.

%package -n texlive-longnamefilelist-doc
Summary:        Documentation for longnamefilelist
Version:        svn27889.0.2

Provides:       tex-longnamefilelist-doc
AutoReqProv:    No

%description -n texlive-longnamefilelist-doc
Documentation for longnamefilelist

%package -n texlive-loops
Provides:       tex-loops = %{tl_version}
License:        LPPL 1.3
Summary:        General looping macros for use with LaTeX
Version:        svn30704.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(skeyval.sty)
Provides:       tex(loops.sty) = %{tl_version}

%description -n texlive-loops
The package provides efficient looping macros for processing
both csv (separated-values) and nsv/tsv (non-separated values)
lists. CSV lists which have associated parsers may be processed
with the tools of the package.

%package -n texlive-loops-doc
Summary:        Documentation for loops
Version:        svn30704.1.3

Provides:       tex-loops-doc
AutoReqProv:    No

%description -n texlive-loops-doc
Documentation for loops

%package -n texlive-lsc
Provides:       tex-lsc = %{tl_version}
License:        LPPL
Summary:        Typesetting Live Sequence Charts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(pstricks.sty), tex(pst-node.sty)
Provides:       tex(lsc.sty) = %{tl_version}

%description -n texlive-lsc
This package is similar to the msc package in that it provides
macros for typesetting a variant of sequence diagrams, in this
case the Live Sequence Charts of Damm and Harel. The package
supports the full LSC language of the original LSC paper, the
Klose-extensions for formal verification and some of the Harel-
extensions for the Play-In/Play-Out approach (cf. the manual).

%package -n texlive-lsc-doc
Summary:        Documentation for lsc
Version:        svn15878.0

Provides:       tex-lsc-doc
AutoReqProv:    No

%description -n texlive-lsc-doc
Documentation for lsc

%package -n texlive-lstaddons
Provides:       tex-lstaddons = %{tl_version}
License:        LPPL 1.3
Summary:        Add-on packages for listings: autogobble and line background
Version:        svn26196.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(listings.sty), tex(xcolor.sty)
Provides:       tex(lstautogobble.sty) = %{tl_version}, tex(lstlinebgrd.sty) = %{tl_version}

%description -n texlive-lstaddons
The bundle contains a small collection of add-on packages for
the listings package. Current packages are: lstlinebgrd: colour
the background of some or all lines of a listing; and
lstautogobble: set the standard "gobble" option to the indent
of the first line of the code.

%package -n texlive-lstaddons-doc
Summary:        Documentation for lstaddons
Version:        svn26196.0.1

Provides:       tex-lstaddons-doc
AutoReqProv:    No

%description -n texlive-lstaddons-doc
Documentation for lstaddons

%package -n texlive-lt3graph
Provides:       tex-lt3graph = %{tl_version}
License:        LPPL 1.3
Summary:        Provide a graph datastructure for experimental LaTeX3
Version:        svn45913
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(filecontents.sty), tex(xparse.sty), tex(etoolbox.sty), tex(withargs.sty)
Requires:       tex(xcolor.sty), tex(mdframed.sty), tex(marginnote.sty), tex(listings.sty)
Requires:       tex(textcomp.sty), tex(hyperref.sty), tex(needspace.sty), tex(noindentafter.sty)
Requires:       tex(ifthen.sty), tex(expl3.sty), tex(l3keys2e.sty)
Provides:       tex(lt3graph-dry.sty) = %{tl_version}, tex(lt3graph-packagedoc.cls) = %{tl_version}
Provides:       tex(lt3graph.sty) = %{tl_version}

%description -n texlive-lt3graph
The package defines a 'graph' data structure, for use in
documents that are using the experimental LaTeX 3 syntax.

%package -n texlive-lt3graph-doc
Summary:        Documentation for lt3graph
Version:        svn45913
Provides:       tex-lt3graph-doc
AutoReqProv:    No

%description -n texlive-lt3graph-doc
Documentation for lt3graph

%package -n texlive-ltablex
Provides:       tex-ltablex = %{tl_version}
License:        LPPL
Summary:        Table package extensions
Version:        svn34923.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty), tex(tabularx.sty)
Provides:       tex(ltablex.sty) = %{tl_version}

%description -n texlive-ltablex
Modifies the tabularx environment to combine the features of
the tabularx package (auto-sized columns in a fixed width
table) with those of the longtable package (multi-page tables).

%package -n texlive-ltablex-doc
Summary:        Documentation for ltablex
Version:        svn34923.1.1

Provides:       tex-ltablex-doc
AutoReqProv:    No

%description -n texlive-ltablex-doc
Documentation for ltablex

%package -n texlive-ltabptch
Provides:       tex-ltabptch = %{tl_version}
License:        LPPL
Summary:        Bug fix for longtable
Version:        svn17533.1.74d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(longtable.sty)
Provides:       tex(ltabptch.sty) = %{tl_version}

%description -n texlive-ltabptch
A patch for LaTeX bugs tools/3180 and tools/3480. The patch
applies to version 4.11 of longtable.

%package -n texlive-ltabptch-doc
Summary:        Documentation for ltabptch
Version:        svn17533.1.74d

Provides:       tex-ltabptch-doc
AutoReqProv:    No

%description -n texlive-ltabptch-doc
Documentation for ltabptch

%package -n texlive-ltxdockit
Provides:       tex-ltxdockit = %{tl_version}
License:        LPPL
Summary:        Documentation support
Version:        svn21869.1.2d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(multicol.sty), tex(keyval.sty), tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(hyperref.sty), tex(hypcap.sty), tex(listings.sty)
Requires:       tex(color.sty), tex(xspace.sty), tex(ifpdf.sty)
Provides:       tex(btxdockit.sty) = %{tl_version}, tex(ltxdockit.cfg) = %{tl_version}
Provides:       tex(ltxdockit.cls) = %{tl_version}, tex(ltxdockit.def) = %{tl_version}
Provides:       tex(ltxdockit.sty) = %{tl_version}

%description -n texlive-ltxdockit
This bundle, consisting of a simple wrapper class and some
packages, forms a small LaTeX/BibTeX documentation kit; the
author uses it for some of his own packages. The package is not
supported: users should not attempt its use unless they are
capable of dealing with problems unaided. (The actual purpose
of releasing the package is to make it possible for third
parties to compile the documentation of other packages, should
that be necessary.)

%package -n texlive-ltxdockit-doc
Summary:        Documentation for ltxdockit
Version:        svn21869.1.2d

Provides:       tex-ltxdockit-doc
AutoReqProv:    No

%description -n texlive-ltxdockit-doc
Documentation for ltxdockit

%package -n texlive-ltxindex
Provides:       tex-ltxindex = %{tl_version}
License:        GPL+
Summary:        A LaTeX package to typeset indices with GNU's Texindex
Version:        svn15878.0.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(multicol.sty)
Provides:       tex(ltxindex.sty) = %{tl_version}

%description -n texlive-ltxindex
A LaTeX package that allows the user to make indexes with GNU's
Texindex program, instead of makeindex. It provides the
indexing commands available in Texinfo by default, but only
defines the concept index (cp) by default -- the user must
define other standard indexes, and there is no provision for
custom indexes. The package is not currently maintained.

%package -n texlive-ltxindex-doc
Summary:        Documentation for ltxindex
Version:        svn15878.0.1c

Provides:       tex-ltxindex-doc
AutoReqProv:    No

%description -n texlive-ltxindex-doc
Documentation for ltxindex

%package -n texlive-ltxkeys
Provides:       tex-ltxkeys = %{tl_version}
License:        LPPL
Summary:        A robust key parser for LaTeX
Version:        svn28332.0.0.3c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty)
Provides:       tex(ltxkeys.sty) = %{tl_version}

%description -n texlive-ltxkeys
The package provides facilities for creating and managing keys
in the sense of the keyval and xkeyval packages, but it is
intended to be more robust and faster. Its robustness comes
from its ability to preserve braces in key values throughout
parsing. The need to preserve braces in key values arises often
in parsing keys (for example, in the xwatermark package). The
package is faster than xkeyval package because (among other
things) it avoids character-wise parsing of key values (called
"selective sanitization" by the xkeyval package). The package
also provides functions for defining and managing keys.

%package -n texlive-ltxkeys-doc
Summary:        Documentation for ltxkeys
Version:        svn28332.0.0.3c

Provides:       tex-ltxkeys-doc
AutoReqProv:    No

%description -n texlive-ltxkeys-doc
Documentation for ltxkeys

%package -n texlive-ltxnew
Provides:       tex-ltxnew = %{tl_version}
License:        LPPL 1.3
Summary:        A simple means of creating commands
Version:        svn21586.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty)
Provides:       tex(ltxnew.sty) = %{tl_version}

%description -n texlive-ltxnew
The package ltxnew provides \new, \renew and \provide prefixes
for checking definitions. It is designed to work with e-TeX
distributions of LaTeX and relies on the LaTeX internal macro
\@ifdefinable. Local allocation of counters, dimensions, skips,
muskips, boxes, tokens and marks are provided by the etex
package. \new and \renew as well as \provide may be used for
all kind of control sequences. Please refer to the section
"Using \new" of the PDF documentation.

%package -n texlive-ltxnew-doc
Summary:        Documentation for ltxnew
Version:        svn21586.1.3

Provides:       tex-ltxnew-doc
AutoReqProv:    No

%description -n texlive-ltxnew-doc
Documentation for ltxnew

%package -n texlive-ltxtools
Provides:       tex-ltxtools = %{tl_version}
License:        LPPL 1.3
Summary:        A collection of LaTeX API macros
Version:        svn24897.0.0.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty), tex(atveryend.sty), tex(ltxkeys.sty), tex(fp.sty)
Provides:       tex(ltxtools-base.sty) = %{tl_version}, tex(ltxtools-doc.sty) = %{tl_version}
Provides:       tex(ltxtools-environ.sty) = %{tl_version}
Provides:       tex(ltxtools-incluput.sty) = %{tl_version}
Provides:       tex(ltxtools-index.sty) = %{tl_version}, tex(ltxtools-review.sty) = %{tl_version}
Provides:       tex(ltxtools-trace.sty) = %{tl_version}, tex(ltxtools.sty) = %{tl_version}

%description -n texlive-ltxtools
This is a bundle of macros that the author uses in the coding
of others of his macro files.

%package -n texlive-ltxtools-doc
Summary:        Documentation for ltxtools
Version:        svn24897.0.0.1a

Provides:       tex-ltxtools-doc
AutoReqProv:    No

%description -n texlive-ltxtools-doc
Documentation for ltxtools

%package -n texlive-lua-check-hyphen
Provides:       tex-lua-check-hyphen = %{tl_version}
License:        MIT
Summary:        Mark hyphenations in a document, for checking
Version:        svn47527
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifluatex.sty), tex(luatexbase-attr.sty)
Requires:       tex(luatextra.sty), tex(keyval.sty)
Provides:       tex(lua-check-hyphen.sty) = %{tl_version}

%description -n texlive-lua-check-hyphen
The package looks at all hyphenation breaks in the document,
comparing them against a white-list prepared by the author. If
a hyphenation break is found, for which there is no entry in
the white-list, the package flags the line where the break
starts. The author may then either add the hyphenation to the
white-list, or adjust the document to avoid the break.

%package -n texlive-lua-check-hyphen-doc
Summary:        Documentation for lua-check-hyphen
Version:        svn47527
Provides:       tex-lua-check-hyphen-doc
AutoReqProv:    No

%description -n texlive-lua-check-hyphen-doc
Documentation for lua-check-hyphen

%package -n texlive-lua-visual-debug
Provides:       tex-lua-visual-debug = %{tl_version}
License:        MIT
Summary:        Visual debugging with LuaLaTeX
Version:        svn41387

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(atbegshi.sty)
Provides:       tex(lua-visual-debug.sty) = %{tl_version}

%description -n texlive-lua-visual-debug
The package uses lua code to provide visible indications of
boxes, glues, kerns and penalties in the PDF output. The
package is known to work in LaTeX and Plain TeX documents.

%package -n texlive-lua-visual-debug-doc
Summary:        Documentation for lua-visual-debug
Version:        svn41387

Provides:       tex-lua-visual-debug-doc
AutoReqProv:    No

%description -n texlive-lua-visual-debug-doc
Documentation for lua-visual-debug

%package -n texlive-luabibentry
Provides:       tex-luabibentry = %{tl_version}
License:        LPPL 1.3
Summary:        Repeat BibTeX entries in a LuaLaTeX document body
Version:        svn31783.0.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty)
Provides:       tex(luabibentry.sty) = %{tl_version}

%description -n texlive-luabibentry
The package reimplements bibentry, for use in LuaLaTeX.

%package -n texlive-luabibentry-doc
Summary:        Documentation for luabibentry
Version:        svn31783.0.1a

Provides:       tex-luabibentry-doc
AutoReqProv:    No

%description -n texlive-luabibentry-doc
Documentation for luabibentry

%package -n texlive-luabidi
Provides:       tex-luabidi = %{tl_version}
License:        LPPL 1.3
Summary:        Bidirectional typesetting with LuaLaTeX
Version:        svn30790.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(arabmaths.tex) = %{tl_version}, tex(autofootnoterule.tex) = %{tl_version}
Provides:       tex(luabidi.sty) = %{tl_version}, tex(textwidthfootnoterule.tex) = %{tl_version}

%description -n texlive-luabidi
The package attempts to emulate the XeTeX bidi package, in teh
context of LuaTeX.

%package -n texlive-luabidi-doc
Summary:        Documentation for luabidi
Version:        svn30790.0.2

Provides:       tex-luabidi-doc
AutoReqProv:    No

%description -n texlive-luabidi-doc
Documentation for luabidi

%package -n texlive-luacode
Provides:       tex-luacode = %{tl_version}
License:        LPPL 1.3
Summary:        Helper for executing lua code from within TeX
Version:        svn25193.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase.sty)
Provides:       tex(luacode.sty) = %{tl_version}

%description -n texlive-luacode
Executing Lua code from within TeX with directlua can sometimes
be tricky: there is no easy way to use the percent character,
counting backslashes may be hard, and Lua comments don't work
the way you expect. The package provides the \luaexec command
and the luacode(*) environments to help with these problems.

%package -n texlive-luacode-doc
Summary:        Documentation for luacode
Version:        svn25193.1.2a

Provides:       tex-luacode-doc
AutoReqProv:    No

%description -n texlive-luacode-doc
Documentation for luacode

%package -n texlive-luaindex
Provides:       tex-luaindex = %{tl_version}
License:        LPPL 1.3
Summary:        Create index using lualatex
Version:        svn25882.0.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase-compat.sty)
Requires:       tex(luatexbase-modutils.sty), tex(scrbase.sty)
Provides:       tex(luaindex.sty) = %{tl_version}

%description -n texlive-luaindex
Luaindex provides (yet another) index processor, written in
Lua.

%package -n texlive-luaindex-doc
Summary:        Documentation for luaindex
Version:        svn25882.0.1b

Provides:       tex-luaindex-doc
AutoReqProv:    No

%description -n texlive-luaindex-doc
Documentation for luaindex

%package -n texlive-luainputenc
Provides:       tex-luainputenc = %{tl_version}
License:        Public Domain
Summary:        Replacing inputenc for use in LuaTeX
Version:        svn20491.0.973

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(ifxetex.sty), tex(inputenc.sty), tex(luatexbase.sty)
Provides:       tex(luainputenc.sty) = %{tl_version}, tex(lutf8.def) = %{tl_version}
Provides:       tex(lutf8x.def) = %{tl_version}

%description -n texlive-luainputenc
LuaTeX operates by default in UTF-8 input; thus LaTeX documents
that need 8-bit character-sets need special treatment. (In
fact, LaTeX documents using UTF-8 with "traditional" -- 256-
glyph -- fonts also need support from this package.) The
package, therefore, replaces the LaTeX standard inputenc for
use under LuaTeX. With a current LuaTeX,the package has the
same behaviour with LuaTeX as inputenc has under pdfTeX.

%package -n texlive-luainputenc-doc
Summary:        Documentation for luainputenc
Version:        svn20491.0.973

Provides:       tex-luainputenc-doc
AutoReqProv:    No

%description -n texlive-luainputenc-doc
Documentation for luainputenc

%package -n texlive-luaintro-doc
Summary:        Documentation for luaintro
Version:        svn35490.0.03

Provides:       tex-luaintro-doc
AutoReqProv:    No

%description -n texlive-luaintro-doc
Documentation for luaintro

%package -n texlive-lualatex-doc-doc
Summary:        Documentation for lualatex-doc
Version:        svn30473.0

Provides:       tex-lualatex-doc-doc
AutoReqProv:    No

%description -n texlive-lualatex-doc-doc
Documentation for lualatex-doc

%package -n texlive-lualatex-math
Provides:       tex-lualatex-math = %{tl_version}
License:        LPPL 1.3
Summary:        Fixes for mathematics-related LuaLaTeX issues
Version:        svn44621
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(etoolbox.sty), tex(luatexbase.sty), tex(filehook.sty)
Provides:       tex(lualatex-math.sty) = %{tl_version}

%description -n texlive-lualatex-math
The package patches a few commands of the LaTeX2e kernel and
the amsmath and mathtools packages to be more compatible with
the LuaTeX engine. It is only meaningful for LuaLaTeX documents
containing mathematical formulas, and does not exhibit any new
functionality. The fixes are mostly moved from the unicode-math
package to this package since they are not directly related to
Unicode mathematics typesetting.

%package -n texlive-lualatex-math-doc
Summary:        Documentation for lualatex-math
Version:        svn44621
Provides:       tex-lualatex-math-doc
AutoReqProv:    No

%description -n texlive-lualatex-math-doc
Documentation for lualatex-math

%package -n texlive-lualibs
Provides:       tex-lualibs = %{tl_version}
License:        GPLv2+
Summary:        Additional Lua functions for LuaTeX macro programmers
Version:        svn43153
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-lualibs
Lualibs is a collection of Lua modules useful for general
programming. The bundle is based on lua modules shipped with
ConTeXt, and are made available in this bundle for use
independent of ConTeXt.

%package -n texlive-lualibs-doc
Summary:        Documentation for lualibs
Version:        svn43153
Provides:       tex-lualibs-doc
AutoReqProv:    No

%description -n texlive-lualibs-doc
Documentation for lualibs

%package -n texlive-luamplib
Provides:       tex-luamplib = %{tl_version}
License:        GPLv2+
Summary:        Use LuaTeX's built-in MetaPost interpreter
Version:        svn47547
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(luatexbase-modutils.sty)
Provides:       tex(luamplib.sty) = %{tl_version}

%description -n texlive-luamplib
The package enables the user to specify MetaPost diagrams
(which may include colour specifications from the color or
xcolor packages) into a document, using LuaTeX's built-in
MetaPost library. The facility is only available in PDF mode.

%package -n texlive-luamplib-doc
Summary:        Documentation for luamplib
Version:        svn47547
Provides:       tex-luamplib-doc
AutoReqProv:    No

%description -n texlive-luamplib-doc
Documentation for luamplib

%package -n texlive-luasseq
Provides:       tex-luasseq = %{tl_version}
License:        LPPL
Summary:        Drawing spectral sequences in LuaLaTeX
Version:        svn37877.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(pifont.sty), tex(pgf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(luasseq.sty) = %{tl_version}

%description -n texlive-luasseq
The package is an update of the author's sseq package, for use
with LuaLaTeX. This version uses less memory, and operates
faster than the original; it also offers several enhancements.

%package -n texlive-luasseq-doc
Summary:        Documentation for luasseq
Version:        svn37877.0

Provides:       tex-luasseq-doc
AutoReqProv:    No

%description -n texlive-luasseq-doc
Documentation for luasseq

%package -n texlive-luatexbase
Provides:       tex-luatexbase = %{tl_version}
License:        Public Domain
Summary:        Basic resource management for LuaTeX code
Version:        svn38550

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatex.sty), tex(etex.sty)
Provides:       tex(luatexbase-attr.sty) = %{tl_version}
Provides:       tex(luatexbase-cctb.sty) = %{tl_version}
Provides:       tex(luatexbase-compat.sty) = %{tl_version}
Provides:       tex(luatexbase-loader.sty) = %{tl_version}
Provides:       tex(luatexbase-mcb.sty) = %{tl_version}, tex(luatexbase-modutils.sty) = %{tl_version}
Provides:       tex(luatexbase-regs.sty) = %{tl_version}
Provides:       tex(luatexbase.sty) = %{tl_version}

%description -n texlive-luatexbase
The bundle provides basic facilities for LuaTeX macro
programmers, mostly resource allocation and convenience
packages. Provided are: luatexbase-attr: attribute allocation;
luatexbase-cctb: catcode table allocation; luatexbase-compat:
compatibility helpers; luatexbase-loader: Lua module loading;
luatexbase-modutils: Lua module declaration; luatexbase-mcb:
callbacks extension; and luatexbase-regs: allocation of
registers and the like. In addition, the (unadorned) luatexbase
package loads all the above in one fell swoop.

%package -n texlive-luatexbase-doc
Summary:        Documentation for luatexbase
Version:        svn38550

Provides:       tex-luatexbase-doc
AutoReqProv:    No

%description -n texlive-luatexbase-doc
Documentation for luatexbase

%package -n texlive-luatexko
Provides:       tex-luatexko = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Korean with Lua(La)TeX
Version:        svn48334
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(luaotfload.sty), tex(fontspec.sty), tex(everysel.sty), tex(kolabels-utf.sty)
Requires:       tex(konames-utf.sty)
Provides:       tex(luatexko-core.sty) = %{tl_version}, tex(luatexko.sty) = %{tl_version}

%description -n texlive-luatexko
This is a Lua(La)TeX macro package that supports typesetting
Korean documents. LuaTeX version 0.76+ and luaotfload package
version 2.2+ are required. This package also requires both cjk-
ko and xetexko packages for its full functionality.

%package -n texlive-luatexko-doc
Summary:        Documentation for luatexko
Version:        svn48334
Provides:       tex-luatexko-doc
AutoReqProv:    No

%description -n texlive-luatexko-doc
Documentation for luatexko

%package -n texlive-luatextra
Provides:       tex-luatextra = %{tl_version}
License:        Public Domain
Summary:        Additional macros for Plain TeX and LaTeX in LuaTeX
Version:        svn20747.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(fontspec.sty), tex(luatexbase.sty), tex(metalogo.sty)
Requires:       tex(luacode.sty), tex(fixltx2e.sty)
Provides:       tex(luatextra.sty) = %{tl_version}

%description -n texlive-luatextra
The package provides a coherent extended programming
environment for use with luaTeX. It loads packages fontspec,
luatexbase and lualibs, and provides additional user-level
features and goodies. The package is under development, and its
specification may be expected to change.

%package -n texlive-luatextra-doc
Summary:        Documentation for luatextra
Version:        svn20747.1.0.1

Provides:       tex-luatextra-doc
AutoReqProv:    No

%description -n texlive-luatextra-doc
Documentation for luatextra

%package -n texlive-luatodonotes
Provides:       tex-luatodonotes = %{tl_version}
License:        LPPL 1.2
Summary:        Add editing annotations in a LuaLaTeX document
Version:        svn45454
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifluatex.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(xcolor.sty)
Requires:       tex(tikz.sty), tex(luacode.sty), tex(luatex.sty), tex(atbegshi.sty)
Requires:       tex(xstring.sty), tex(zref-abspage.sty), tex(ifoddpage.sty), tex(soul.sty)
Requires:       tex(soulpos.sty)
Provides:       tex(luatodonotes.sty) = %{tl_version}

%description -n texlive-luatodonotes
The package allows the user to insert comments into a document
that suggest (for example) further editing that may be needed.
The comments are shown in the margins alongside the text;
different styles for the comments may be used; the styles are
selected using package options. The package is based on the
package todonotes, and depends heavily on Lua, so it can only
be used with LuaLaTeX.

%package -n texlive-luatodonotes-doc
Summary:        Documentation for luatodonotes
Version:        svn45454
Provides:       tex-luatodonotes-doc
AutoReqProv:    No

%description -n texlive-luatodonotes-doc
Documentation for luatodonotes

%package -n texlive-luaxml
Provides:       tex-luaxml = %{tl_version}
License:        MIT
Summary:        Lua library for reading and serialising XML files
Version:        svn48215
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-luaxml
This is a redistribution of a pure lua xml library, LuaXML
(this version supports Lua 5.2). The library was originally
distributed as part of the odsfile package, but is made
available separately in the hope that it can be useful for
other projects.

%package -n texlive-luaxml-doc
Summary:        Documentation for luaxml
Version:        svn48215
Provides:       tex-luaxml-doc
AutoReqProv:    No

%description -n texlive-luaxml-doc
Documentation for luaxml

%package -n texlive-logicproof
Provides:       tex-logicproof = %{tl_version}
License:        LPPL 1.3
Summary:        Box proofs for propositional and predicate logic
Version:        svn33254.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(ifthen.sty)
Provides:       tex(logicproof.sty) = %{tl_version}

%description -n texlive-logicproof
A common style of proof used in propositional and predicate
logic is Fitch proofs, in which each line of the proof has a
statement and a justification, and subproofs within a larger
proof have boxes around them. The package provides environments
for typesetting such proofs and boxes. It creates proofs in a
style similar to that used in "Logic in Computer Science" by
Huth and Ryan.

%package -n texlive-logicproof-doc
Summary:        Documentation for logicproof
Version:        svn33254.0

Provides:       tex-logicproof-doc
AutoReqProv:    No

%description -n texlive-logicproof-doc
Documentation for logicproof

%package -n texlive-lpform
Provides:       tex-lpform = %{tl_version}
License:        LPPL
Summary:        Typesetting linear programming formulations and sets of equations
Version:        svn36918.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lpform.sty) = %{tl_version}

%description -n texlive-lpform
The package is designed to aid the author writing linear
programming formulations, one restriction at a time. With the
package, one can easily label equations, formulations can span
multiple pages and several elements of the layout (such as
spacing, texts and equation tags) are also customizable.
Besides linear programming formulations, this package can also
be used to display any series of aligned equations with easy
labeling/referencing and other customization options.

%package -n texlive-lpform-doc
Summary:        Documentation for lpform
Version:        svn36918.0

Provides:       tex-lpform-doc
AutoReqProv:    No

%description -n texlive-lpform-doc
Documentation for lpform

%package -n texlive-lplfitch
Provides:       tex-lplfitch = %{tl_version}
License:        LPPL 1.3
Summary:        Fitch-style natural deduction proofs
Version:        svn31077.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lplfitch.sty) = %{tl_version}

%description -n texlive-lplfitch
The package provides macros for typesetting natural deduction
proofs in "Fitch" style, with subproofs indented and offset by
scope lines. The proofs from use of the package are in the
format used in the textbook Language, Proof, and Logic by Dave
Barker-Plummer, Jon Barwise, and John Etchemendy.

%package -n texlive-lplfitch-doc
Summary:        Documentation for lplfitch
Version:        svn31077.0.9

Provides:       tex-lplfitch-doc
AutoReqProv:    No

%description -n texlive-lplfitch-doc
Documentation for lplfitch

%package -n texlive-latexmp
Provides:       tex-latexmp = %{tl_version}
License:        Public Domain
Summary:        Interface for LaTeX-based typesetting in MetaPost
Version:        svn15878.1.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-latexmp
The MetaPost package latexMP implements a user-friendly
interface to access LaTeX-based typesetting capabilities in
MetaPost. The text to be typeset is given as string. This
allows even dynamic text elements, for example counters, to be
used in labels. Compared to other implementations it is much
more flexible, since it can be used as direct replacement for
btex..etex, and much faster, compared for example to the
solution provided by tex.mp

%package -n texlive-latexmp-doc
Summary:        Documentation for latexmp
Version:        svn15878.1.2.1

Provides:       tex-latexmp-doc
AutoReqProv:    No

%description -n texlive-latexmp-doc
Documentation for latexmp

%package -n texlive-lps
Provides:       tex-lps = %{tl_version}
License:        LPPL
Summary:        Class for "Logic and Philosophy of Science"
Version:        svn21322.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mathptmx.sty), tex(geometry.sty), tex(titlesec.sty), tex(titletoc.sty)
Requires:       tex(lastpage.sty), tex(caption.sty)
Provides:       tex(lps.cls) = %{tl_version}

%description -n texlive-lps
The 'Logic and Philosophy of Science' journal is an online
publication of the University of Trieste (Italy). The class
builds on the standard article class to offer a format that
LaTeX authors may use when submitting to the journal.

%package -n texlive-lps-doc
Summary:        Documentation for lps
Version:        svn21322.0.7

Provides:       tex-lps-doc
AutoReqProv:    No

%description -n texlive-lps-doc
Documentation for lps

%package -n texlive-langsci-doc
Provides:       tex-langsci-doc = %{tl_version}
License:        LPPL
Summary:        doc files of langsci
Version:        svn47487
AutoReqProv:    No

%description -n texlive-langsci-doc
Documentation for langsci

%package -n texlive-langsci
Provides:       tex-langsci = %{tl_version}
License:        LPPL
Summary:        Typeset books for publication with Language Science Press
Version:        svn47487
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(langscibook.cls) = %{tl_version}, tex(langsci-cgloss.sty) = %{tl_version}
Provides:       tex(langsci-bidi.sty) = %{tl_version}, tex(langsci-tbls.sty) = %{tl_version}
Provides:       tex(langsci-basic.sty) = %{tl_version}, tex(langsci-gb4e.sty) = %{tl_version}
Provides:       tex(langsci-optional.sty) = %{tl_version}
Provides:       tex(langsci-forest-setup.sty) = %{tl_version}
Provides:       tex(langsci-advertisement.tex) = %{tl_version}
Provides:       tex(langsci-series.def) = %{tl_version}, tex(langsci-colors.def) = %{tl_version}

%description -n texlive-langsci
This packages allows you to typeset monographs and edited
volumes for publication with Language Science Press
(http://www.langsci-press.org). It includes all necessary files
for title pages, frontmatter, main content, list of references
and indexes. Dust jackets for BoD and Createspace (print-on-
demand service providers) can also be produced.

%package -n texlive-latex2e-help-texinfo-fr-doc
Provides:       tex-latex2e-help-texinfo-fr-doc = %{tl_version}
License:        LPPL
Summary:        doc files of latex2e-help-texinfo-fr
Version:        svn44997
AutoReqProv:    No

%description -n texlive-latex2e-help-texinfo-fr-doc
Documentation for latex2e-help-texinfo-fr

%package -n texlive-latex-bib2-ex-doc
Provides:       tex-latex-bib2-ex-doc = %{tl_version}
License:        LPPL
Summary:        doc files of latex-bib2-ex
Version:        svn40098

AutoReqProv:    No

%description -n texlive-latex-bib2-ex-doc
Documentation for latex-bib2-ex

%package -n texlive-latex-tds-doc
Provides:       tex-latex-tds-doc = %{tl_version}
License:        LPPL
Summary:        doc files of latex-tds
Version:        svn40613

AutoReqProv:    No

%description -n texlive-latex-tds-doc
Documentation for latex-tds

%package -n texlive-libertinegc-doc
Provides:       tex-libertinegc-doc = %{tl_version}
License:        LPPL
Summary:        doc files of libertinegc
Version:        svn44616
AutoReqProv:    No

%description -n texlive-libertinegc-doc
Documentation for libertinegc

%package -n texlive-libertinegc
Provides:       tex-libertinegc = %{tl_version}
License:        LPPL
Summary:        Libertine add-on to support Greek and Cyrillic
Version:        svn44616
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(libertinegc.sty) = %{tl_version}, tex(libertinegc.map) = %{tl_version}
Provides:       tex(LGRLinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(LGRLinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(T2BLinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(LGRLinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(LGRLinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(T2CLinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(T2BLinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(T2ALinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(T2CLinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(OT2LinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(OT2LinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(OT2LinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(OT2LinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(T2ALinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(T2BLinuxLibertineT-TOsF.fd) = %{tl_version}
Provides:       tex(T2ALinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(T2ALinuxLibertineT-TLF.fd) = %{tl_version}
Provides:       tex(T2CLinuxLibertineT-LF.fd) = %{tl_version}
Provides:       tex(T2BLinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(T2CLinuxLibertineT-OsF.fd) = %{tl_version}
Provides:       tex(libtlf-lgr.enc) = %{tl_version}, tex(lib-t2a.enc) = %{tl_version}
Provides:       tex(lib-t2b.enc) = %{tl_version}, tex(lib-t2a1.enc) = %{tl_version}
Provides:       tex(lib-t2a2.enc) = %{tl_version}, tex(libosf-lgr.enc) = %{tl_version}
Provides:       tex(lib-t2b1.enc) = %{tl_version}, tex(lib-t2c.enc) = %{tl_version}
Provides:       tex(lib1-ot2.enc) = %{tl_version}, tex(lib-t2b2.enc) = %{tl_version}
Provides:       tex(lib-t2c1.enc) = %{tl_version}, tex(lib-ot2.enc) = %{tl_version}
Provides:       tex(lib-t2c2.enc) = %{tl_version}, tex(LinLibertineTI-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-t2b.tfm) = %{tl_version}
Provides:       tex(LinLIbertineT-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTB-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBO-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZ-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTI-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineTO-t2c.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-t2a.tfm) = %{tl_version}
Provides:       tex(LinLibertineT-t2b.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZI-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-ot2.tfm) = %{tl_version}
Provides:       tex(LinLibertineTZO-osf-lgr.tfm) = %{tl_version}
Provides:       tex(LinLibertineTBI-osf-lgr.tfm) = %{tl_version}

%description -n texlive-libertinegc
The package provides LaTeX support files to access the Greek
and Cyrillic glyphs in LinuxLibertine. It functions as an add-
on to the libertine package, using filenames and macro names
that are compatible with that package. Supported encodings:
LGR, T2A, T2B, T2C, OT2.

%package -n texlive-libertinus-doc
Provides:       tex-libertinus-doc = %{tl_version}
License:        OFL
Summary:        doc files of libertinus
Version:        svn47488
AutoReqProv:    No

%description -n texlive-libertinus-doc
Documentation for libertinus

%package -n texlive-libertinust1math-doc
Provides:       tex-libertinust1math-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of libertinust1math
Version:        svn48077
AutoReqProv:    No

%description -n texlive-libertinust1math-doc
Documentation for libertinust1math

%package -n texlive-libertinust1math
Provides:       tex-libertinust1math = %{tl_version}
License:        LPPL and OFL
Summary:        A Type 1 font and LaTeX support for Libertinus Math
Version:        svn48077
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(libertinust1math.sty) = %{tl_version}
Provides:       tex(libertinust1math.map) = %{tl_version}
Provides:       tex(ot1libertinust1mathsf.fd) = %{tl_version}
Provides:       tex(ls2libertinust1mathex.fd) = %{tl_version}
Provides:       tex(ls2libertinust1mathsym.fd) = %{tl_version}
Provides:       tex(ls1libertinust1math.fd) = %{tl_version}
Provides:       tex(LibertinusT1Math.pfb) = %{tl_version}
Provides:       tex(libusSYM.enc) = %{tl_version}, tex(libusSFI.enc) = %{tl_version}
Provides:       tex(libusEX.enc) = %{tl_version}, tex(libusMR.enc) = %{tl_version}
Provides:       tex(libusBMI.enc) = %{tl_version}, tex(libusSFB.enc) = %{tl_version}
Provides:       tex(libusBMR.enc) = %{tl_version}, tex(libusSF.enc) = %{tl_version}
Provides:       tex(libusBB.enc) = %{tl_version}, tex(libusFRK.enc) = %{tl_version}
Provides:       tex(libusMI.enc) = %{tl_version}, tex(libertinust1-mathsym.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathbb.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathrm.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathsfb.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathex.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathsfi.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathrm-bold.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathsf.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathit-bold.tfm) = %{tl_version}
Provides:       tex(libertinust1-mathit.tfm) = %{tl_version}

%description -n texlive-libertinust1math
The package provides a Type1 version of Libertinus Math, with a
number of additions and changes, plus LaTeX support files that
allow it to serve as a math accompaniment to Libertine under
LaTeX.

%package -n texlive-libertinus
Provides:       tex-libertinus = %{tl_version}
License:        OFL
Summary:        The Libertinus font family
Version:        svn47488
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(libertinusserifinitials-regular.otf) = %{tl_version}
Provides:       tex(libertinussans-bold.otf) = %{tl_version}
Provides:       tex(libertinusserif-italic.otf) = %{tl_version}
Provides:       tex(libertinussans-regular.otf) = %{tl_version}
Provides:       tex(libertinusserif-regular.otf) = %{tl_version}
Provides:       tex(libertinusserif-semibold.otf) = %{tl_version}
Provides:       tex(libertinusserif-semibolditalic.otf) = %{tl_version}
Provides:       tex(libertinuskeyboard-regular.otf) = %{tl_version}
Provides:       tex(libertinusmath-regular.otf) = %{tl_version}
Provides:       tex(libertinusserif-bold.otf) = %{tl_version}
Provides:       tex(libertinussans-italic.otf) = %{tl_version}
Provides:       tex(libertinusmono-regular.otf) = %{tl_version}
Provides:       tex(libertinusserifdisplay-regular.otf) = %{tl_version}
Provides:       tex(libertinusserif-bolditalic.otf) = %{tl_version}

%description -n texlive-libertinus
This is a fork of the Linux Libertine and Linux Biolinum fonts
that started as an OpenType math companion of the Libertine
font family, but grown as a full fork to address some of the
bugs in the fonts. The family consists of: Libertinus Serif:
forked from Linux Libertine. Libertinus Sans: forked from Linux
Biolinum. Libertinus Mono: forked from Linux Libertine Mono.
Libertinus Math: an OpenType math font for use in OpenType math-
capable applications like LuaTeX, XeTeX or MS Word 2007+.

%package -n texlive-librebodoni-doc
Provides:       tex-librebodoni-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of librebodoni
Version:        svn39375

AutoReqProv:    No

%description -n texlive-librebodoni-doc
Documentation for librebodoni

%package -n texlive-librebodoni
Provides:       tex-librebodoni = %{tl_version}
License:        LPPL and OFL
Summary:        Libre Bodoni fonts with LaTeX support
Version:        svn39375

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(LibreBodoni.sty) = %{tl_version}, tex(LibreBodoni.map) = %{tl_version}
Provides:       tex(T1LibreBodoni-Sup.fd) = %{tl_version}
Provides:       tex(LY1LibreBodoni-Inf.fd) = %{tl_version}
Provides:       tex(LY1LibreBodoni-TLF.fd) = %{tl_version}
Provides:       tex(T1LibreBodoni-Inf.fd) = %{tl_version}
Provides:       tex(OT1LibreBodoni-Inf.fd) = %{tl_version}
Provides:       tex(T1LibreBodoni-TLF.fd) = %{tl_version}
Provides:       tex(LY1LibreBodoni-Sup.fd) = %{tl_version}
Provides:       tex(TS1LibreBodoni-TLF.fd) = %{tl_version}
Provides:       tex(OT1LibreBodoni-Sup.fd) = %{tl_version}
Provides:       tex(OT1LibreBodoni-TLF.fd) = %{tl_version}
Provides:       tex(LibreBodoni-Bold.pfb) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic.pfb) = %{tl_version}
Provides:       tex(LibreBodoni-Italic.pfb) = %{tl_version}
Provides:       tex(LibreBodoni-Regular.pfb) = %{tl_version}
Provides:       tex(lbd_zpaflu.enc) = %{tl_version}, tex(lbd_dwvqiv.enc) = %{tl_version}
Provides:       tex(lbd_gxeqsi.enc) = %{tl_version}, tex(lbd_yeotsr.enc) = %{tl_version}
Provides:       tex(lbd_k2dfwc.enc) = %{tl_version}, tex(lbd_rpuqof.enc) = %{tl_version}
Provides:       tex(lbd_2nc6ly.enc) = %{tl_version}, tex(lbd_fttd7q.enc) = %{tl_version}
Provides:       tex(lbd_oaf34p.enc) = %{tl_version}, tex(lbd_pcwse4.enc) = %{tl_version}
Provides:       tex(LibreBodoni-Bold.otf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular.otf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic.otf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic.otf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(LibreBodoni-Regular-tlf-ts1.tfm) = %{tl_version}

%description -n texlive-librebodoni
The Libre Bodoni fonts are designed by Pablo Impallari and
Rodrigo Fuenzalida, based on the 19th century Morris Fuller
Benton's.

%package -n texlive-linop-doc
Provides:       tex-linop-doc = %{tl_version}
License:        LPPL
Summary:        doc files of linop
Version:        svn41304

AutoReqProv:    No

%description -n texlive-linop-doc
Documentation for linop

%package -n texlive-linop
Provides:       tex-linop = %{tl_version}
License:        LPPL
Summary:        Typeset linear operators as they appear in quantum theory or linear algebra
Version:        svn41304

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(linop.sty) = %{tl_version}

%description -n texlive-linop
This small package aims to provide two simple commands and many
options to easily write linear operators as they appear in many-
body physics, quantum theory, and linear algebra, in any of the
ways commonly in use.

%package -n texlive-longfbox-doc
Provides:       tex-longfbox-doc = %{tl_version}
License:        LPPL
Summary:        doc files of longfbox
Version:        svn39028

AutoReqProv:    No

%description -n texlive-longfbox-doc
Documentation for longfbox

%package -n texlive-longfbox
Provides:       tex-longfbox = %{tl_version}
License:        LPPL
Summary:        Draw framed boxes with standard CSS attributes that can break over multiple pages
Version:        svn39028

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(longfbox.sty) = %{tl_version}, tex(longbox.sty) = %{tl_version}

%description -n texlive-longfbox
The longfbox package provides framed boxes that can be
customized using standard CSS attributes. It was written to
support precise rendering of Madoko documents in LaTeX.

%package -n texlive-lroundrect-doc
Provides:       tex-lroundrect-doc = %{tl_version}
License:        LPPL
Summary:        doc files of lroundrect
Version:        svn39804

AutoReqProv:    No

%description -n texlive-lroundrect-doc
Documentation for lroundrect

%package -n texlive-lroundrect
Provides:       tex-lroundrect = %{tl_version}
License:        LPPL
Summary:        LaTeX macros for utilizing the roundrect MetaPost routines
Version:        svn39804

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lroundrect.sty) = %{tl_version}

%description -n texlive-lroundrect
This LaTeX package provides ways to use the extremely
configurable rounded rectangles of the roundrect MetaPost
package with LaTeX. It is chiefly useful for examples, but also
has macros for particular types of boxes which are useful on
their own.

%package -n texlive-lshort-estonian-doc
Provides:       tex-lshort-estonian-doc = %{tl_version}
License:        GPLv2+
Summary:        doc files of lshort-estonian
Version:        svn39323

AutoReqProv:    No

%description -n texlive-lshort-estonian-doc
Documentation for lshort-estonian

%package -n texlive-lstbayes-doc
Provides:       tex-lstbayes-doc = %{tl_version}
License:        LPPL
Summary:        doc files of lstbayes
Version:        svn48160
AutoReqProv:    No

%description -n texlive-lstbayes-doc
Documentation for lstbayes

%package -n texlive-lstbayes
Provides:       tex-lstbayes = %{tl_version}
License:        LPPL
Summary:        Listings language driver for Bayesian modeling languages
Version:        svn48160
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(lstbayes.sty) = %{tl_version}

%description -n texlive-lstbayes
The package provides language drivers for the listings package
for several languages not included in that package: BUGS, JAGS,
and Stan.

%package -n texlive-luatex85-doc
Provides:       tex-luatex85-doc = %{tl_version}
License:        LPPL
Summary:        doc files of luatex85
Version:        svn41395

AutoReqProv:    No

%description -n texlive-luatex85-doc
Documentation for luatex85

%package -n texlive-luatex85
Provides:       tex-luatex85 = %{tl_version}
License:        LPPL
Summary:        pdfTeX aliases for LuaTeX
Version:        svn41395

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(luatex85.sty) = %{tl_version}

%description -n texlive-luatex85
The package provides emulation of pdfTeX primitives for LuaTeX
v0.85+.

%package -n texlive-listofitems
Summary:        Grab items in lists using user-specified sep char
Version:        svn46962
License:        LPPL
Requires:       texlive-base, texlive-kpathsea
Provides:       tex(listofitems.sty) = %{tl_version}, tex(listofitems.tex) = %{tl_version}

%description -n texlive-listofitems
This simple package is designed to read a list of items whose
parsing character may be selected by the user. Once the list is
read, its items are stored in a structure that behaves as a
dimensioned array. As such, it becomes very easy to access an
item in the list by its number. For example, if the list is
stored in the macro \foo, the item #3 is designated by \foo[3].
A component may, in turn, be a list with a parsing delimiter
different from the parent list, paving the way for nesting and
employing a syntax reminiscent of an array of several
dimensions of the type \foo[3,2] to access the item #2 of the
list contained within the item #3 of the top-tier list.

%package -n texlive-ladder
Summary:        Draw simple ladder diagrams using TikZ
Version:        svn44394
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ladder.sty) = %{tl_version}

%description -n texlive-ladder
This package permits the creation of simple ladder diagrams
within LaTeX documents. Required packages are tikz, ifthen, and
calc.

%package -n texlive-latexbangla
Summary:        Enhanced LaTeX integration for Bangla
Version:        svn42409
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(latexbangla.sty) = %{tl_version}

%description -n texlive-latexbangla
This package simplifies the process of writing Bangla in LaTeX
and addresses most of the associated typesetting issues.
Notable features: Automated transition from Bangla to English
and vice versa. Patch for the unproportionate whitespace issue
in popular Bangla fonts. Full support for all the common
commands and environments. Bangla numbering for page, section,
chapter, footnotes etc. (extending polyglossia's support). New
theorem, problems, example, solution and other environments,
all of which are in Bangla.

%package -n texlive-latexbug
Summary:        Bug-classification for LaTeX related bugs
Version:        svn45559
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(latexbug.sty) = %{tl_version}

%description -n texlive-latexbug
The package is written in order to help identifying the
rightful addressee for a bug report. The LaTeX team asks that
it will be loaded in any test file that is intended to be sent
to the LaTeX bug database as part of a bug report.

%package -n texlive-latexgit
Summary:        A LaTeX git wrapper
Version:        svn41920
License:        gpl3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(latexgit.sty) = %{tl_version}

%description -n texlive-latexgit
This package provides several macros to fetch git information
and typeset it. The macros defined by LaTeXgit can be helpful
to documentation authors and others to whom clear document
versioning is important.

%package -n texlive-latex-mr-doc
Summary:        A practical guide to LaTeX and Polyglossia for Marathi and other Indian languages
Version:        svn44601
License:        LPPL

%description -n texlive-latex-mr-doc
The package provides a short guide to LaTeX and specifically to the
polyglossia package. This document aims to introduce LaTeX and polyglossia for
Indian languages. Though the document often discusses the language Marathi,
the discussion applies to other India languages also, with some minute changes
which are described in Section 1.2. We assume that the user of this document
knows basic (La)TeX or has, at least, tried her hand on it. This document is
not very suitable for first time users.

%package -n texlive-latex-refsheet-doc
Summary:        Reference sheet for a thesis with the KOMAScript document classes
Version:        svn45076
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(LaTeX_RefSheet.tex) = %{tl_version}, tex(acknowledgements.tex) = %{tl_version}
Provides:       tex(header-graph.tex) = %{tl_version}, tex(thesis.tex) = %{tl_version}

%description -n texlive-latex-refsheet-doc
This LaTeX Reference Sheet is for writing a thesis with the KOMAScript
document classes (scrartcl, scrreprt, scrbook) and all the packages
which a thesis in the natural sciences needs.

%package -n texlive-limecv
Summary:        a (Xe/Lua)LaTeX document class for curriculum vitae
Version:        svn45906
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(limecv.cls) = %{tl_version}

%description -n texlive-limecv
limecv is a (Xe/Lua)LaTeX document class to write curriculum
vitae. It is designed with the following design rules: simple,
elegant and clean. To this end, it offers several environments
and macros for convenience.

%package -n texlive-ling-macros
Summary:        Macros for typesetting formal linguistics
Version:        svn42268
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ling-macros.sty) = %{tl_version}

%description -n texlive-ling-macros
This package contains macros for typesetting glosses and formal
expressions. It covers a range of subfields in formal
linguistics.

%package -n texlive-lion-msc
Summary:        LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of Physics (LION).
Version:        svn44131
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lion-msc.cls) = %{tl_version}

%description -n texlive-lion-msc
LaTeX class for B.Sc. and M.Sc. reports at Leiden Institute of
Physics (LION). The purpose of this class is twofold: It
creates a uniform layout of the student theses from our
department. More importantly it contains several fields on the
front-page that the user needs to fill that are used in the
university administration (name, student number and name of
supervisor) Students are free to change the layout of the text
but should leave the title page as it is.

%package -n texlive-lni
Summary:        Official class for the "Lecture Notes in Informatics"
Version:        svn48133
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lni.cls) = %{tl_version}

%description -n texlive-lni
This is the official version of the class "lni" for submissions
to the Lecture Notes in Informatics published by the
Gesellschaft fur Informatik. It is based on previous templates
created on behalf of the GI.

%package -n texlive-ltb2bib
Summary:        converts amsrefs' .ltb bibliographical databases to BibTeX format
Version:        svn43746
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ltb2bib.sty) = %{tl_version}

%description -n texlive-ltb2bib
This package implements a LaTeX command that converts an
amsrefs bibliographical database (.ltb) to a BibTeX
bibliographical database (.bib). ltb2bib is the reverse of the
"amsxport" option in amsrefs. Typical uses are: produce bib
entries for some publishers which don't accept amsrefs (Taylor
& Francis, for example); import an ltb database in a database
management program, e.g. for sorting; access one's ltb database
within emacs's RefTeX mode.

%package -n texlive-luahyphenrules
Summary:        Loading patterns in LuaLaTeX with language.dat
Version:        svn42670
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(luahyphenrules.sty) = %{tl_version}

%description -n texlive-luahyphenrules
Preloading hyphenation patterns (or 'hyphen rules.) into any
format based upon LuaTeX is not required in LuaTeX and recent
releases of babel don't do it anyway. This package is addressed
to those who just want to select the languages and load their
patterns by means of `language.dat` without loading `babel`.

%package -n texlive-luamesh
Summary:        Computes and draws 2D Delaunay triangulation
Version:        svn43814
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(luamesh.sty) = %{tl_version}

%description -n texlive-luamesh
The package allows to compute and draw 2D Delaunay
triangulation. The algorithm is written with lua, and depending
upon the choice of the engine, the drawing is done by MetaPost
(with luamplib) or by TikZ. The Delaunay triangulation
algorithm is the Bowyer and Watson algorithm. Several macros
are provided to draw the global mesh, the set of points, or a
particular step of the algorithm.

%package -n texlive-luapackageloader
Summary:        Allow LuaTeX to load external Lua packages
Version:        svn44865
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(luapackageloader.sty) = %{tl_version}

%description -n texlive-luapackageloader
This package allows LuaTeX to load packages from the default
package.path and package.cpath locations. This could be useful
to load external Lua modules, including modules installed via
LuaRocks. This package requires ifluatex.

%package -n texlive-labelschanged
Summary:        Identify labels which cause endless "may have changed" warnings
Version:        svn46040
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(labelschanged.sty) = %{tl_version}

%description -n texlive-labelschanged
Several conditions can cause LaTeX labels to keep changing, no
matter how many times a document is recompiled. This package
helps diagnose the cause of repeated "Label(s) may have
changed" warnings. The names and before/after definitions of
changing labels are printed at the end of each compile.
Multiply-defined labels are printed as well.

%package -n texlive-latex-via-exemplos
Summary:        A LaTeX course written in brazilian portuguese language
Version:        svn48038
License:        GPLv2+
Requires:       texlive-base texlive-kpathsea

%description -n texlive-latex-via-exemplos
This is a LaTeX2e course written in brazilian portuguese
language.

%package -n texlive-lccaps
Summary:        Lowercased (spaced) small capitals
Version:        svn46432
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lccaps.sty) = %{tl_version}

%description -n texlive-lccaps
This little package serves the purpose of providing a uniform
method to use lowercased small capitals and spaced lowercased
small capitals. It relies on the iftex, textcase, and microtype
packages and comes with four new user macros: \textlcc, the
main feature: lowercased small capitals; \spacedcaps, a prefix
to small capitals text commands to slightly increase their
spacing; \textslcc and \textssc, which are shortcuts for
\spacedcaps\textlcc and \spacedcaps\textsc (accordingly).

%package -n texlive-libertinus-otf
Summary:        Support for Libertinus OpenType
Version:        svn48464
License:        LPPL and OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(libertinusmath-bold.otf) = %{tl_version}
Provides:       tex(libertinusmono-bold.otf) = %{tl_version}
Provides:       tex(libertinusmono-bolditalic.otf) = %{tl_version}
Provides:       tex(libertinusmono-italic.otf) = %{tl_version}
Provides:       tex(libertinussans-bolditalic.otf) = %{tl_version}
Provides:       tex(libertinus-otf.sty) = %{tl_version}

%description -n texlive-libertinus-otf
This package offers LuaLaTeX/XeLaTeX support for the Libertinus
OpenType fonts maintained by Khaled Hosny. Furthermore
math-bold, mono-bold, mono-oblique, and mono-bold-oblique font
styles are provided, which have been derived from the ones in
the libertinus package itself. The Libertinus fonts are
similiar to Libertine and Biolinum, but come with math symbols.

%package -n texlive-llncsconf
Summary:        LaTeX package extending Springer's llcns class
Version:        svn46707
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(llncsconf.sty) = %{tl_version}

%description -n texlive-llncsconf
The package extends Springer's llncs class for adding
additional notes describing the status of the paper (submitted,
accepted) as well as for creating author-archived versions that
include the references to the official version hosted by
Springer (as requested by the copyright transfer agreement for
Springer's LNCS series).

%package -n texlive-longdivision
Summary:        Long division arithmetic problems
Version:        svn43159
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(xparse.sty)
Provides:       tex(longdivision.sty) = %{tl_version}

%description -n texlive-longdivision
This package solves long division problems and typesets the
solutions. The dividend must be a positive decimal number and
the divisor must be a positive integer. Repeating decimals is
handled correctly, putting a bar over the repeated part of the
decimal. Dividends up to 20 digits long are handled gracefully
(though the typeset result will take up about a page), and
dividends between 20 and 60 digits long slightly less
gracefully. The package defines two macros, \longdivision and
\intlongdivision. Each takes two arguments, a dividend and a
divisor. \longdivision keeps dividing until the remainder is
zero, or it encounters a repeated remainder. \intlongdivision
stops when the dividend stops (though the dividend doesn't have
to be an integer). This package depends on the xparse package
from the l3packages bundle.

%package -n texlive-lualatex-truncate
Summary:        A wrapper for using the truncate package with LuaLaTeX
Version:        svn48469
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lualatex-truncate.sty) = %{tl_version}

%description -n texlive-lualatex-truncate
This package provides a wrapper for the truncate package, thus
fixing issues related to LuaTeX's hyphenation algorithm.

%package -n texlive-luavlna
Summary:        Prevent line breaks after single letter words, units, or adademic titles
Version:        svn47892
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(luavlna-csplain-langs.lua) = %{tl_version}
Provides:       tex(luavlna-langno.lua) = %{tl_version}, tex(luavlna-predegrees.lua) = %{tl_version}
Provides:       tex(luavlna-presi.lua) = %{tl_version}, tex(luavlna-si.lua) = %{tl_version}
Provides:       tex(luavlna-sufdegrees.lua) = %{tl_version}
Provides:       tex(luavlna.4ht) = %{tl_version}, tex(luavlna.lua) = %{tl_version}
Provides:       tex(luavlna.sty) = %{tl_version}

%description -n texlive-luavlna
In some languages, like Czech or Polish, there should be no
single letter words at the end of a line, according to
typographical norms. This package handles such situations using
LuaTeX's callback mechanism. In doing this, the package can
detect languages used in the text and insert spaces only in
parts of the document where languages requiring this feature
are used. Another feature of this package is the inclusion of
non-breakable space after initials (like in personal names),
after or before academic degrees, and between numbers and
units. The package supports both plain LuaTeX and LuaLaTeX.
BTW: "vlna" is the Czech word for "wave" or "curl" and also
denotes the tilde which, in TeX, is used for "unbreakable
spaces".

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="impallari/librebaskerville impallari/librecaslon \
impallari/lobster2 public/libertine public/lm public/lm-math"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
mv %{buildroot}/%{_texdir}/texmf-dist/doc/info/* %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*


%files -n texlive-latexconfig
%{_texdir}/texmf-dist/tex/latex/latexconfig/

%files -n texlive-latex-fonts
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/latex-fonts/
%{_texdir}/texmf-dist/fonts/tfm/public/latex-fonts/

%files -n texlive-latex-fonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/latex-fonts/

%files -n texlive-lambda
%{_texdir}/texmf-dist/tex/lambda/

%files -n texlive-lua-alt-getopt
%{_texdir}/texmf-dist/scripts/lua-alt-getopt/

%files -n texlive-lua-alt-getopt-doc
%{_texdir}/texmf-dist/doc/support/lua-alt-getopt/

%files -n texlive-ltxmisc
%license collection.txt
%{_texdir}/texmf-dist/tex/latex/ltxmisc/

%files -n texlive-logreq
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/logreq/

%files -n texlive-logreq-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/logreq/

%files -n texlive-lm
%license gfsl.txt
%{_datadir}/fonts/lm
%{_texdir}/texmf-dist/fonts/afm/public/lm/
%{_texdir}/texmf-dist/fonts/enc/dvips/lm/
%{_texdir}/texmf-dist/fonts/map/dvipdfm/lm/
%{_texdir}/texmf-dist/fonts/map/dvips/lm/
%{_texdir}/texmf-dist/fonts/opentype/public/lm/
%{_texdir}/texmf-dist/fonts/tfm/public/lm/
%{_texdir}/texmf-dist/fonts/type1/public/lm/
%{_texdir}/texmf-dist/tex/latex/lm/

%files -n texlive-lm-doc
%license gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/lm/

%files -n texlive-lm-math
%license gfl.txt
%{_datadir}/fonts/lm-math
%{_texdir}/texmf-dist/fonts/opentype/public/lm-math/

%files -n texlive-lm-math-doc
%license gfl.txt
%{_texdir}/texmf-dist/doc/fonts/lm-math/

%files -n texlive-lato
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/lato/
%{_texdir}/texmf-dist/fonts/map/dvips/lato/
%{_texdir}/texmf-dist/fonts/tfm/typoland/lato/
%{_texdir}/texmf-dist/fonts/truetype/typoland/lato/
%{_texdir}/texmf-dist/fonts/type1/typoland/lato/
%{_texdir}/texmf-dist/fonts/vf/typoland/lato/
%{_texdir}/texmf-dist/tex/latex/lato/

%files -n texlive-lato-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/lato/

%files -n texlive-lfb
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/lfb/
%{_texdir}/texmf-dist/fonts/tfm/public/lfb/

%files -n texlive-lfb-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/lfb/

%files -n texlive-libertine
%license lppl1.txt
%{_datadir}/fonts/libertine
%{_texdir}/texmf-dist/fonts/enc/dvips/libertine/
%{_texdir}/texmf-dist/fonts/map/dvips/libertine/
%{_texdir}/texmf-dist/fonts/opentype/public/libertine/
%{_texdir}/texmf-dist/fonts/tfm/public/libertine/
%{_texdir}/texmf-dist/fonts/type1/public/libertine/
%{_texdir}/texmf-dist/fonts/vf/public/libertine/
%{_texdir}/texmf-dist/tex/latex/libertine/

%files -n texlive-libertine-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/libertine/

%files -n texlive-librebaskerville
%license lppl1.txt
%{_datadir}/fonts/librebaskerville
%{_texdir}/texmf-dist/fonts/enc/dvips/librebaskerville/
%{_texdir}/texmf-dist/fonts/map/dvips/librebaskerville/
%{_texdir}/texmf-dist/fonts/opentype/impallari/librebaskerville/
%{_texdir}/texmf-dist/fonts/tfm/impallari/librebaskerville/
%{_texdir}/texmf-dist/fonts/type1/impallari/librebaskerville/
%{_texdir}/texmf-dist/fonts/vf/impallari/librebaskerville/
%{_texdir}/texmf-dist/tex/latex/librebaskerville/

%files -n texlive-librebaskerville-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/librebaskerville/

%files -n texlive-librecaslon
%license ofl.txt
%{_datadir}/fonts/librecaslon
%{_texdir}/texmf-dist/fonts/enc/dvips/librecaslon/
%{_texdir}/texmf-dist/fonts/map/dvips/librecaslon/
%{_texdir}/texmf-dist/fonts/opentype/impallari/librecaslon/
%{_texdir}/texmf-dist/fonts/tfm/impallari/librecaslon/
%{_texdir}/texmf-dist/fonts/type1/impallari/librecaslon/
%{_texdir}/texmf-dist/fonts/vf/impallari/librecaslon/
%{_texdir}/texmf-dist/tex/latex/librecaslon/

%files -n texlive-librecaslon-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/librecaslon/

%files -n texlive-libris
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/libris/
%{_texdir}/texmf-dist/fonts/enc/dvips/libris/
%{_texdir}/texmf-dist/fonts/map/dvips/libris/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/libris/
%{_texdir}/texmf-dist/fonts/type1/arkandis/libris/
%{_texdir}/texmf-dist/fonts/vf/arkandis/libris/
%{_texdir}/texmf-dist/tex/latex/libris/

%files -n texlive-libris-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/libris/

%files -n texlive-lineara
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/linearA/
%{_texdir}/texmf-dist/fonts/map/dvips/linearA/
%{_texdir}/texmf-dist/fonts/tfm/public/linearA/
%{_texdir}/texmf-dist/fonts/type1/public/linearA/
%{_texdir}/texmf-dist/tex/latex/linearA/

%files -n texlive-lineara-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/linearA/

%files -n texlive-lobster2
%license ofl.txt
%{_datadir}/fonts/lobster2
%{_texdir}/texmf-dist/fonts/enc/dvips/lobster2/
%{_texdir}/texmf-dist/fonts/map/dvips/lobster2/
%{_texdir}/texmf-dist/fonts/opentype/impallari/lobster2/
%{_texdir}/texmf-dist/fonts/tfm/impallari/lobster2/
%{_texdir}/texmf-dist/fonts/truetype/impallari/lobster2/
%{_texdir}/texmf-dist/fonts/type1/impallari/lobster2/
%{_texdir}/texmf-dist/fonts/vf/impallari/lobster2/
%{_texdir}/texmf-dist/tex/latex/lobster2/

%files -n texlive-lobster2-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/lobster2/

%files -n texlive-lxfonts
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/lxfonts/
%{_texdir}/texmf-dist/fonts/source/public/lxfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/lxfonts/
%{_texdir}/texmf-dist/fonts/type1/public/lxfonts/
%{_texdir}/texmf-dist/tex/latex/lxfonts/

%files -n texlive-lxfonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/lxfonts/

%files -n texlive-ly1
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/ly1/
%{_texdir}/texmf-dist/fonts/map/dvips/ly1/
%{_texdir}/texmf-dist/fonts/tfm/adobe/ly1/
%{_texdir}/texmf-dist/fonts/vf/adobe/ly1/
%{_texdir}/texmf-dist/tex/latex/ly1/
%{_texdir}/texmf-dist/tex/plain/ly1/

%files -n texlive-ly1-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/ly1/

%files -n texlive-labyrinth
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/labyrinth/

%files -n texlive-labyrinth-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/labyrinth/

%files -n texlive-logicpuzzle
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/logicpuzzle/
%{_texdir}/texmf-dist/tex/latex/logicpuzzle/

%files -n texlive-logicpuzzle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/logicpuzzle/

%files -n texlive-lambda-lists
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/lambda-lists/

%files -n texlive-lambda-lists-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/lambda-lists/

%files -n texlive-langcode
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/langcode/

%files -n texlive-langcode-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/langcode/

%files -n texlive-lecturer
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/lecturer/

%files -n texlive-lecturer-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/lecturer/

%files -n texlive-librarian
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/librarian/

%files -n texlive-librarian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/librarian/

%files -n texlive-ledmac
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ledmac/

%files -n texlive-ledmac-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ledmac/

%files -n texlive-leipzig
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/leipzig/
%{_texdir}/texmf-dist/makeindex/leipzig/

%files -n texlive-leipzig-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/leipzig/

%files -n texlive-lexref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lexref/

%files -n texlive-lexref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lexref/

%files -n texlive-linguex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/linguex/

%files -n texlive-linguex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/linguex/

%files -n texlive-liturg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/liturg/

%files -n texlive-liturg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/liturg/

%files -n texlive-lshort-persian-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-persian/

%files -n texlive-latex-notes-zh-cn-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/latex-notes-zh-cn/

%files -n texlive-lshort-chinese-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-chinese/

%files -n texlive-lcyw
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lcyw/

%files -n texlive-lcyw-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lcyw/

%files -n texlive-lh
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/lh/
%{_texdir}/texmf-dist/tex/latex/lh/
%{_texdir}/texmf-dist/tex/plain/lh/

%files -n texlive-lh-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/lh/

%files -n texlive-lhcyr
%{_texdir}/texmf-dist/tex/latex/lhcyr/

%files -n texlive-lshort-bulgarian-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-bulgarian/

%files -n texlive-lshort-mongol-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lshort-mongol/

%files -n texlive-lshort-russian-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-russian/

%files -n texlive-lshort-ukr-doc
%{_texdir}/texmf-dist/doc/latex/lshort-ukr/

%files -n texlive-lshort-czech-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-czech/

%files -n texlive-lshort-slovak-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lshort-slovak/


%files -n texlive-l2tabu-english-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/l2tabu-english/

%files -n texlive-latex-brochure-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latex-brochure/

%files -n texlive-latex-course-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/latex-course/

%files -n texlive-latex-doc-ptr-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/latex-doc-ptr/

%files -n texlive-latex-graphics-companion-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latex-graphics-companion/

%files -n texlive-latex-veryshortguide-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latex-veryshortguide/

%files -n texlive-latex-web-companion-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latex-web-companion/

%files -n texlive-latex2e-help-texinfo
%{_infodir}/latex2e.info*

%files -n texlive-latex2e-help-texinfo-doc
%{_texdir}/texmf-dist/doc/latex/latex2e-help-texinfo/

%files -n texlive-latex4wp-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/latex4wp/

%files -n texlive-latexcheat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latexcheat/

%files -n texlive-latexcourse-rug-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/latexcourse-rug/

%files -n texlive-latexfileinfo-pkgs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/latexfileinfo-pkgs/

%files -n texlive-latexfileinfo-pkgs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/latexfileinfo-pkgs/

%files -n texlive-lshort-english-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/lshort-english/

%files -n texlive-lithuanian
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/lithuanian/
%{_texdir}/texmf-dist/fonts/map/dvips/lithuanian/
%{_texdir}/texmf-dist/fonts/tfm/public/lithuanian/
%{_texdir}/texmf-dist/tex/latex/lithuanian/

%files -n texlive-lithuanian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lithuanian/

%files -n texlive-lshort-dutch-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-dutch/

%files -n texlive-lshort-finnish-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-finnish/

%files -n texlive-lshort-slovenian-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-slovenian/

%files -n texlive-lshort-turkish-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-turkish/

%files -n texlive-l2tabu-french-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/l2tabu-french/

%files -n texlive-lshort-french-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-french/

%files -n texlive-l2picfaq-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/l2picfaq/

%files -n texlive-l2tabu-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/l2tabu/

%files -n texlive-latex-bib-ex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/latex-bib-ex/

%files -n texlive-latex-referenz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/latex-referenz/

%files -n texlive-latex-tabellen-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latex-tabellen/

%files -n texlive-latexcheat-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latexcheat-de/

%files -n texlive-lshort-german-doc
%{_texdir}/texmf-dist/doc/latex/lshort-german/

%files -n texlive-lualatex-doc-de-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/lualatex-doc-de/

%files -n texlive-levy
%license gpl2.txt
%{_texdir}/texmf-dist/fonts/source/public/levy/
%{_texdir}/texmf-dist/fonts/tfm/public/levy/
%{_texdir}/texmf-dist/tex/generic/levy/

%files -n texlive-levy-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/levy/

%files -n texlive-lgreek
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/lgreek/

%files -n texlive-lgreek-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/lgreek/

%files -n texlive-l2tabu-italian-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/l2tabu-italian/

%files -n texlive-latex4wp-it-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/latex4wp-it/

%files -n texlive-layaureo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/layaureo/

%files -n texlive-layaureo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/layaureo/

%files -n texlive-lshort-italian-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-italian/

%files -n texlive-lshort-japanese-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-japanese/

%files -n texlive-luatexja
%license bsd.txt
%{_texdir}/texmf-dist/tex/luatex/luatexja/

%files -n texlive-luatexja-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/luatex/luatexja/

%files -n texlive-lshort-korean-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/lshort-korean/

%files -n texlive-lshort-thai-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-thai/

%files -n texlive-lshort-vietnamese-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lshort-vietnamese/

%files -n texlive-lshort-polish-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-polish/

%files -n texlive-latexcheat-ptbr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latexcheat-ptbr/

%files -n texlive-lshort-portuguese-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lshort-portuguese/

%files -n texlive-l2tabu-spanish-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/l2tabu-spanish/

%files -n texlive-latex2e-help-texinfo-spanish
%{_infodir}/latex2e-es.info*

%files -n texlive-latex2e-help-texinfo-spanish-doc
%{_texdir}/texmf-dist/doc/latex/latex2e-help-texinfo-spanish/

%files -n texlive-latexcheat-esmx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/latexcheat-esmx/

%files -n texlive-lshort-spanish-doc
%{_texdir}/texmf-dist/doc/latex/lshort-spanish/

%files -n texlive-l3kernel
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/l3kernel/

%files -n texlive-l3kernel-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/l3kernel/

%files -n texlive-l3packages
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/l3packages/

%files -n texlive-l3packages-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/l3packages/

%files -n texlive-l3experimental
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/l3experimental/

%files -n texlive-l3experimental-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/l3experimental/

%files -n texlive-lineno
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/lineno/

%files -n texlive-lineno-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lineno/

%files -n texlive-listings
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/listings/

%files -n texlive-listings-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/listings/

%files -n texlive-lapdf
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/lapdf/

%files -n texlive-lapdf-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lapdf/

%files -n texlive-latex-make
%license gpl.txt
%{_texdir}/texmf-dist/scripts/latex-make/
%{_texdir}/texmf-dist/tex/latex/latex-make/

%files -n texlive-latex-make-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/support/latex-make/

%files -n texlive-lpic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lpic/

%files -n texlive-lpic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lpic/

%files -n texlive-labbook
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/labbook/

%files -n texlive-labbook-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/labbook/

%files -n texlive-labels
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/labels/

%files -n texlive-labels-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/labels/

%files -n texlive-lastpackage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lastpackage/

%files -n texlive-lastpackage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lastpackage/

%files -n texlive-lastpage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lastpage/

%files -n texlive-lastpage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lastpage/

%files -n texlive-latexdemo
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/latexdemo/

%files -n texlive-latexdemo-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/latexdemo/

%files -n texlive-layouts
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/layouts/

%files -n texlive-layouts-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/layouts/

%files -n texlive-lazylist
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/lazylist/

%files -n texlive-lazylist-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/lazylist/

%files -n texlive-lcd
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/lcd/

%files -n texlive-lcd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lcd/

%files -n texlive-lcg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/lcg/

%files -n texlive-lcg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lcg/

%files -n texlive-leading
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/leading/

%files -n texlive-leading-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/leading/

%files -n texlive-leaflet
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/leaflet/

%files -n texlive-leaflet-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/leaflet/

%files -n texlive-leftidx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/leftidx/

%files -n texlive-leftidx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/leftidx/

%files -n texlive-lengthconvert
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lengthconvert/

%files -n texlive-lengthconvert-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lengthconvert/

%files -n texlive-lettre
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lettre/

%files -n texlive-lettre-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lettre/

%files -n texlive-lettrine
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lettrine/

%files -n texlive-lettrine-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lettrine/

%files -n texlive-lewis
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/lewis/

%files -n texlive-lewis-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/lewis/

%files -n texlive-lhelp
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/lhelp/

%files -n texlive-lhelp-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lhelp/

%files -n texlive-libgreek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/libgreek/

%files -n texlive-libgreek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/libgreek/

%files -n texlive-limap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/limap/

%files -n texlive-linegoal
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/linegoal/

%files -n texlive-linegoal-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/linegoal/

%files -n texlive-lipsum
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/lipsum/

%files -n texlive-lipsum-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lipsum/

%files -n texlive-lisp-on-tex
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/lisp-on-tex/

%files -n texlive-lisp-on-tex-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/latex/lisp-on-tex/

%files -n texlive-listing
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/listing/

%files -n texlive-listing-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/listing/

%files -n texlive-listlbls
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/listlbls/

%files -n texlive-listlbls-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/listlbls/

%files -n texlive-listliketab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/listliketab/

%files -n texlive-listliketab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/listliketab/

%files -n texlive-listofsymbols
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/listofsymbols/

%files -n texlive-listofsymbols-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/listofsymbols/

%files -n texlive-lkproof
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/lkproof/

%files -n texlive-lkproof-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/lkproof/

%files -n texlive-lmake
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/lmake/

%files -n texlive-lmake-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/lmake/

%files -n texlive-locality
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/locality/

%files -n texlive-locality-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/locality/

%files -n texlive-localloc
%{_texdir}/texmf-dist/tex/latex/localloc/

%files -n texlive-localloc-doc
%{_texdir}/texmf-dist/doc/latex/localloc/

%files -n texlive-logbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/logbox/

%files -n texlive-logbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/logbox/

%files -n texlive-logical-markup-utils
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/logical-markup-utils/

%files -n texlive-logical-markup-utils-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/logical-markup-utils/

%files -n texlive-logpap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/logpap/

%files -n texlive-logpap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/logpap/

%files -n texlive-longfigure
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/longfigure/

%files -n texlive-longfigure-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/longfigure/

%files -n texlive-longnamefilelist
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/longnamefilelist/

%files -n texlive-longnamefilelist-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/longnamefilelist/

%files -n texlive-loops
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/loops/

%files -n texlive-loops-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/loops/

%files -n texlive-lsc
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/lsc/
%{_texdir}/texmf-dist/tex/latex/lsc/

%files -n texlive-lsc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lsc/

%files -n texlive-lstaddons
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lstaddons/

%files -n texlive-lstaddons-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lstaddons/

%files -n texlive-lt3graph
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lt3graph/

%files -n texlive-lt3graph-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lt3graph/

%files -n texlive-ltablex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ltablex/

%files -n texlive-ltablex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ltablex/

%files -n texlive-ltabptch
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ltabptch/

%files -n texlive-ltabptch-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ltabptch/

%files -n texlive-ltxdockit
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ltxdockit/

%files -n texlive-ltxdockit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ltxdockit/

%files -n texlive-ltxindex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/ltxindex/

%files -n texlive-ltxindex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ltxindex/

%files -n texlive-ltxkeys
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ltxkeys/

%files -n texlive-ltxkeys-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ltxkeys/

%files -n texlive-ltxnew
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ltxnew/

%files -n texlive-ltxnew-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ltxnew/

%files -n texlive-ltxtools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ltxtools/

%files -n texlive-ltxtools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ltxtools/

%files -n texlive-lua-check-hyphen
%license other-free.txt
%{_texdir}/texmf-dist/tex/lualatex/lua-check-hyphen/

%files -n texlive-lua-check-hyphen-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/lualatex/lua-check-hyphen/

%files -n texlive-lua-visual-debug
%license other-free.txt
%{_texdir}/texmf-dist/tex/luatex/lua-visual-debug/

%files -n texlive-lua-visual-debug-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/luatex/lua-visual-debug/

%files -n texlive-luabibentry
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/luabibentry/

%files -n texlive-luabibentry-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/luabibentry/

%files -n texlive-luabidi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/luabidi/

%files -n texlive-luabidi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/luabidi/

%files -n texlive-luacode
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/luacode/

%files -n texlive-luacode-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/luacode/

%files -n texlive-luaindex
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/luaindex/
%{_texdir}/texmf-dist/tex/lualatex/luaindex/

%files -n texlive-luaindex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/luaindex/

%files -n texlive-luainputenc
%license pd.txt
%{_texdir}/texmf-dist/tex/lualatex/luainputenc/

%files -n texlive-luainputenc-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/lualatex/luainputenc/

%files -n texlive-luaintro-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/luatex/luaintro/

%files -n texlive-lualatex-doc-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/lualatex/lualatex-doc/

%files -n texlive-lualatex-math
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/lualatex-math/

%files -n texlive-lualatex-math-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/lualatex-math/

%files -n texlive-lualibs
%license gpl2.txt
%{_texdir}/texmf-dist/tex/luatex/lualibs/

%files -n texlive-lualibs-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/luatex/lualibs/

%files -n texlive-luamplib
%license gpl2.txt
%{_texdir}/texmf-dist/tex/luatex/luamplib/

%files -n texlive-luamplib-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/luatex/luamplib/

%files -n texlive-luasseq
%license lppl1.txt
%{_texdir}/texmf-dist/scripts/luasseq/
%{_texdir}/texmf-dist/tex/lualatex/luasseq/

%files -n texlive-luasseq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/lualatex/luasseq/

%files -n texlive-luatexbase
%license pd.txt
%{_texdir}/texmf-dist/tex/luatex/luatexbase/

%files -n texlive-luatexbase-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/luatex/luatexbase/

%files -n texlive-luatexko
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/luatex/luatexko/

%files -n texlive-luatexko-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/luatex/luatexko/

%files -n texlive-luatextra
%license pd.txt
%{_texdir}/texmf-dist/tex/lualatex/luatextra/

%files -n texlive-luatextra-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/lualatex/luatextra/

%files -n texlive-luatodonotes
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/lualatex/luatodonotes/

%files -n texlive-luatodonotes-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/lualatex/luatodonotes/

%files -n texlive-luaxml
%license other-free.txt
%{_texdir}/texmf-dist/tex/luatex/luaxml/

%files -n texlive-luaxml-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/luatex/luaxml/

%files -n texlive-logicproof
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/logicproof/

%files -n texlive-logicproof-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/logicproof/

%files -n texlive-lpform
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/lpform/

%files -n texlive-lpform-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/lpform/

%files -n texlive-lplfitch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lplfitch/

%files -n texlive-lplfitch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lplfitch/

%files -n texlive-latexmp
%license pd.txt
%{_texdir}/texmf-dist/metapost/latexmp/

%files -n texlive-latexmp-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/latexmp/

%files -n texlive-leadsheets
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/leadsheets/

%files -n texlive-leadsheets-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/leadsheets/

%files -n texlive-lps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/lps/

%files -n texlive-lps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/lps/

%files -n texlive-langsci-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/langsci/

%files -n texlive-langsci
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/langsci/
%{_texdir}/texmf-dist/bibtex/bst/langsci/

%files -n texlive-latex2e-help-texinfo-fr-doc
%license lppl.txt
%{_infodir}/latex2e-fr.info*
%{_texdir}/texmf-dist/doc/latex/latex2e-help-texinfo-fr/

%files -n texlive-latex-bib2-ex-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/latex-bib2-ex/

%files -n texlive-latex-tds-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/latex-tds/

%files -n texlive-libertinegc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/libertinegc/

%files -n texlive-libertinegc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/libertinegc/
%{_texdir}/texmf-dist/fonts/map/dvips/libertinegc/
%{_texdir}/texmf-dist/fonts/tfm/public/libertinegc/
%{_texdir}/texmf-dist/fonts/enc/dvips/libertinegc/

%files -n texlive-libertinus-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/libertinus/

%files -n texlive-libertinust1math-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/libertinust1math/

%files -n texlive-libertinust1math
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/libertinust1math/
%{_texdir}/texmf-dist/fonts/map/dvips/libertinust1math/
%{_texdir}/texmf-dist/fonts/tfm/public/libertinust1math/
%{_texdir}/texmf-dist/fonts/enc/dvips/libertinust1math/
%{_texdir}/texmf-dist/fonts/afm/public/libertinust1math/
%{_texdir}/texmf-dist/fonts/type1/public/libertinust1math/
%{_texdir}/texmf-dist/fonts/vf/public/libertinust1math/

%files -n texlive-libertinus
%license ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/libertinus/

%files -n texlive-librebodoni-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/librebodoni/

%files -n texlive-librebodoni
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/librebodoni/
%{_texdir}/texmf-dist/fonts/opentype/impallari/librebodoni/
%{_texdir}/texmf-dist/fonts/map/dvips/librebodoni/
%{_texdir}/texmf-dist/fonts/tfm/impallari/librebodoni/
%{_texdir}/texmf-dist/fonts/vf/impallari/librebodoni/
%{_texdir}/texmf-dist/fonts/enc/dvips/librebodoni/
%{_texdir}/texmf-dist/fonts/type1/impallari/librebodoni/

%files -n texlive-linop-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/linop/

%files -n texlive-linop
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/linop/

%files -n texlive-longfbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/longfbox/

%files -n texlive-longfbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/longfbox/

%files -n texlive-lroundrect-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lroundrect/

%files -n texlive-lroundrect
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lroundrect/

%files -n texlive-lshort-estonian-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/lshort-estonian/

%files -n texlive-lstbayes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/lstbayes/

%files -n texlive-lstbayes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/lstbayes/

%files -n texlive-luatex85-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/luatex85/

%files -n texlive-luatex85
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/luatex85/

%files -n texlive-listofitems
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/listofitems/
%doc %{_texdir}/texmf-dist/doc/generic/listofitems/

%files -n texlive-ladder
%doc %{_texdir}/texmf-dist/doc/latex/ladder/
%{_texdir}/texmf-dist/tex/latex/ladder/

%files -n texlive-latexbangla
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/latexbangla/
%{_texdir}/texmf-dist/tex/latex/latexbangla/

%files -n texlive-latexbug
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/latexbug/
%{_texdir}/texmf-dist/tex/latex/latexbug/

%files -n texlive-latexgit
%license gpl3.txt
%doc %{_texdir}/texmf-dist/doc/latex/latexgit/
%{_texdir}/texmf-dist/tex/latex/latexgit/

%files -n texlive-latex-mr-doc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/latex-mr/

%files -n texlive-latex-refsheet-doc
%doc %{_texdir}/texmf-dist/doc/latex/latex-refsheet/

%files -n texlive-limecv
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/limecv/
%{_texdir}/texmf-dist/tex/latex/limecv/

%files -n texlive-ling-macros
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ling-macros/
%{_texdir}/texmf-dist/tex/latex/ling-macros/

%files -n texlive-lion-msc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/lion-msc/
%{_texdir}/texmf-dist/bibtex/bst/lion-msc/
%{_texdir}/texmf-dist/tex/latex/lion-msc/

%files -n texlive-lni
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/lni/
%{_texdir}/texmf-dist/bibtex/bst/lni/
%{_texdir}/texmf-dist/tex/latex/lni/

%files -n texlive-ltb2bib
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/ltb2bib/
%{_texdir}/texmf-dist/tex/latex/ltb2bib/

%files -n texlive-luahyphenrules
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/lualatex/luahyphenrules/
%{_texdir}/texmf-dist/tex/lualatex/luahyphenrules/

%files -n texlive-luamesh
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/lualatex/luamesh/
%{_texdir}/texmf-dist/scripts/luamesh/
%{_texdir}/texmf-dist/tex/lualatex/luamesh/

%files -n texlive-luapackageloader
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/luatex/luapackageloader/
%{_texdir}/texmf-dist/tex/luatex/luapackageloader/

%files -n texlive-labelschanged
%{_texdir}/texmf-dist/tex/latex/labelschanged/
%doc %{_texdir}/texmf-dist/doc/latex/labelschanged/

%files -n texlive-latex-via-exemplos
%license gpl2.txt
%doc %{_texdir}/texmf-dist/doc/latex/latex-via-exemplos/

%files -n texlive-lccaps
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/lccaps/
%doc %{_texdir}/texmf-dist/doc/latex/lccaps/

%files -n texlive-libertinus-otf
%license lppl.txt ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/libertinus-otf/
%{_texdir}/texmf-dist/tex/latex/libertinus-otf/
%doc %{_texdir}/texmf-dist/doc/fonts/libertinus-otf/

%files -n texlive-llncsconf
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/llncsconf/
%doc %{_texdir}/texmf-dist/doc/latex/llncsconf/

%files -n texlive-longdivision
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/longdivision/
%doc %{_texdir}/texmf-dist/doc/latex/longdivision/

%files -n texlive-lualatex-truncate
%license lppl.txt
%{_texdir}/texmf-dist/tex/lualatex/lualatex-truncate/
%doc %{_texdir}/texmf-dist/doc/lualatex/lualatex-truncate/

%files -n texlive-luavlna
%license lppl.txt
%{_texdir}/texmf-dist/tex/luatex/luavlna/
%doc %{_texdir}/texmf-dist/doc/luatex/luavlna/

%changelog
* Mon Aug 23 2021 caodongxia <caodongxia@huawei.com> - 8:2018-25
- Remove texlive-lexikon who requires texlive-wsuipa

* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
