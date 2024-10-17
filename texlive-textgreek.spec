Name:		texlive-textgreek
Version:	44192
Release:	2
Summary:	Upright greek letters in text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textgreek.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
