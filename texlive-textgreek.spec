# revision 24282
# category Package
# catalog-ctan /macros/latex/contrib/textgreek
# catalog-date 2011-10-13 09:47:13 +0200
# catalog-license lppl
# catalog-version v0.7
Name:		texlive-textgreek
Version:	v0.7
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Use upright greek letters as text symbols, e.g. \textbeta.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textgreek/textgreek.sty
%doc %{_texmfdistdir}/doc/latex/textgreek/README
%doc %{_texmfdistdir}/doc/latex/textgreek/textgreek.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textgreek/textgreek.dtx
%doc %{_texmfdistdir}/source/latex/textgreek/textgreek.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
