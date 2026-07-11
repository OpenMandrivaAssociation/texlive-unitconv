%global tl_name unitconv
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Convert a length into one with another unit
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/unitconv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unitconv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unitconv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines two macros to convert a value with unit into one
with another unit. Supported are all TeX-related units, and also km and
m. The output can be in scientific notation for large values. The
package only works with LuaLaTeX!

