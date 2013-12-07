# revision 24282
# category Package
# catalog-ctan /macros/latex/contrib/textgreek
# catalog-date 2011-10-13 09:47:13 +0200
# catalog-license lppl
# catalog-version v0.7
Name:		texlive-textgreek
Version:	v0.7
Release:	5
Summary:	Upright greek letters in text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Use upright greek letters as text symbols, e.g. \textbeta.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textgreek/textgreek.sty
%doc %{_texmfdistdir}/doc/latex/textgreek/README
%doc %{_texmfdistdir}/doc/latex/textgreek/textgreek.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textgreek/textgreek.dtx
%doc %{_texmfdistdir}/source/latex/textgreek/textgreek.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.7-2
+ Revision: 756786
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.7-1
+ Revision: 719717
- texlive-textgreek
- texlive-textgreek
- texlive-textgreek

