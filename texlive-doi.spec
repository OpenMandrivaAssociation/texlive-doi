%global tl_name doi
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Create correct hyperlinks for DOI numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/doi
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
You can hyperlink DOI numbers to doi.org. However, some publishers have
elected to use nasty characters in their DOI numbering scheme ('<', '>',
'_' and ';' have all been spotted). This will either upset (La)TeX, or
your PDF reader. This package contains a single user-level command
\doi{}, which takes a DOI number, and creates a correct hyperlink to the
target of the DOI.

