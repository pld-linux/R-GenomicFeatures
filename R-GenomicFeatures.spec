%define		packname	GenomicFeatures

Summary:	Tools for making and manipulating transcript centric annotations
Name:		R-%{packname}
Version:	1.12.1
Release:	1
License:	Artistic 2.0
Group:		Applications/Math
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	b9cfb7e3d3c32092834a9fbd5a4de212
URL:		http://www.bioconductor.org/packages/release/bioc/html/GenomicRanges.html
BuildRequires:	R
BuildRequires:	R-AnnotationDbi >= 1.19.36
BuildRequires:	R-BiocGenerics
BuildRequires:	R-GenomicRanges >= 1.11.11
BuildRequires:	R-IRanges-devel >= 1.17.13
BuildRequires:	R-Biostrings
BuildRequires:	R-rtracklayer
BuildRequires:	R-biomaRt
BuildRequires:	R-cran-RCurl
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-AnnotationDbi >= 1.19.36
Requires:	R-BiocGenerics
Requires:	R-GenomicRanges >= 1.11.11
Requires:	R-IRanges >= 1.17.13
Requires:	R-Biostrings
Requires:	R-rtracklayer
Requires:	R-biomaRt
Requires:	R-cran-RCurl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of tools and methods for making and manipulating transcript
centric annotations. With these tools the user can easily download
the genomic locations of the transcripts, exons and cds of a given
organism, from either the UCSC Genome Browser or a BioMart database
(more sources will be supported in the future). This information is
then stored in a local database that keeps track of the relationship
between transcripts, exons, cds and genes. Flexible methods are
provided for extracting the desired features in a convenient format.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/extdata/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/script
%{_libdir}/R/library/%{packname}/txdb-template
