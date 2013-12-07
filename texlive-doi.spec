# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/doi
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-doi
Version:	20080818
Release:	5
Summary:	Create correct hyperlinks for DOI numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/doi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
You can hyperlink DOI numbers to dx.doi.org. However, some
publishers have elected to use nasty characters in their DOI
numbering scheme ('<', '>', '_' and ';' have all been spotted).
This will either upset (La)TeX, or your PDF reader. This
package contains a single user-level command \doi{}, which
takes a DOI number, and creates a correct hyperlink from it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/doi/doi.sty
%doc %{_texmfdistdir}/doc/latex/doi/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080818-2
+ Revision: 751010
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080818-1
+ Revision: 718246
- texlive-doi
- texlive-doi
- texlive-doi
- texlive-doi

